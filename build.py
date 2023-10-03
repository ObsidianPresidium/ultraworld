import os
import datetime
import shutil

original_directory = os.getcwd()

script_path = os.path.dirname(os.path.realpath(__file__))
# Create build directory
now = datetime.datetime.now()
build_path = script_path + "/build-" + now.strftime("%d%m%y-%H%M")
if os.path.exists(build_path):
    os.rmdir(build_path)
os.mkdir(build_path)


# Crawl
def crawler(directory_to_crawl: str):
    previous_working_directory = os.getcwd()
    ignore = ["__pycache__"]
    os.chdir(directory_to_crawl)

    def crawl(directory):
        crawl_results = []
        for file in os.listdir(directory):
            file_path = os.path.abspath(file)
            if file not in ignore:
                if os.path.isdir(file_path):
                    previous_working_directory_crawl = os.getcwd()
                    os.chdir(file_path)
                    crawl_results += crawl(file_path)
                    os.chdir(previous_working_directory_crawl)
                else:
                    crawl_results.append(file_path)
        return crawl_results

    to_return = crawl(directory_to_crawl)
    os.chdir(previous_working_directory)
    return to_return


copy_targets = []
copy_targets += crawler(script_path + "/src")
for file in copy_targets:
    shutil.copyfile(file, build_path + "/" + os.path.basename(file))


# Build the application
os.chdir(build_path)
os.system("pyinstaller --clean -y --onefile main.py")
# Remove any unnecessary files
for file in os.listdir(build_path):
    if file not in ["build", "dist", "main.spec"]:
        if os.path.isdir(file):
            os.rmdir(file)
        else:
            os.remove(file)
os.chdir(original_directory)