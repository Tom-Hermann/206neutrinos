##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-206neutrinos-tom.hermann
## File description:
## error
##

from sys import stderr
from src.constante import *

def print_usage(exit_value):
    print()
    exit(exit_value)

def error(argv):
    if len(argv) <= 0 or len(argv) > 4:
        print_usage(FAILURE)

    for i in argv:
        try:
            float(i)
        except:
            if (i == "-h" or i == "--help"):
                print_usage(SUCCESS)
            else:
                print_usage(FAILURE)
        if float(i) < 0:
            print("{} must be postiv".format(i), file=stderr)
            exit(FAILURE)
    if len(argv) != 4:
        exit(FAILURE)