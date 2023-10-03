import readchar
import sys

using_pseudo_terminal = not sys.stdout.isatty()
if using_pseudo_terminal:
    getch_backend = input
    print("You are using a pseudo-terminal. getch calls be replaced with input calls.")
else:
    getch_backend = readchar.readchar


def getch(string_to_print):
    if not string_to_print:
        return getch_backend()
    else:
        print("\r" + string_to_print, end="")
        output = getch_backend()
        if not using_pseudo_terminal:
            print()
        return output


def option_menu(charfuncdict: dict, string_to_print=": "):
    # Takes these inputs:
    #   list of characters and functions: [{"{CHAR}": function}]
    answer = getch(string_to_print)
    answer = answer.lower()
    return charfuncdict[answer]()
