#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
##
## File description:
## main
##

from sys import argv
from src.error import error
from src.constante import *
from src.calcul import *

def get_value():
    new = input("Enter next value: ")
    try:
        float(new)
    except:
        if (new.capitalize() == "End"):
            exit(SUCCESS)
        exit(FAILURE)
    if float(new) < 0:
        print("Number must be positiv", file=stderr)
        exit(FAILURE)
    return float(new)


def boucle(value):
    while(1):
        new = get_value()
        save = value[ARITHMETIC_MEAN]
        value[NUMBER_VALUES] += 1
        mean_square = calcul_QMean(value[NUMBER_VALUES], new, value[ARITHMETIC_MEAN], value[STANDARD_DEVIATION])
        value[ARITHMETIC_MEAN] = calcul_AMean(value[NUMBER_VALUES], new, value[ARITHMETIC_MEAN])
        value[STANDARD_DEVIATION] = calcul_Sd(value[NUMBER_VALUES], new, value[STANDARD_DEVIATION], value[ARITHMETIC_MEAN], save)
        value[HARMONIC_MEAN] = calcul_HMean(value[NUMBER_VALUES], new, value[HARMONIC_MEAN])
        print("\tNumber of values:\t{}".format(int(value[NUMBER_VALUES])))
        print("\tStandard deviation:\t{:.2f}".format(value[STANDARD_DEVIATION]))
        print("\tArithmetic mean:\t{:.2f}".format(value[ARITHMETIC_MEAN]))
        print("\tRoot mean square:\t{:.2f}".format(mean_square))
        print("\tHarmonic mean:\t\t{:.2f}\n".format(value[HARMONIC_MEAN]))




def main():
    error(argv[1:])
    boucle([float(i) for i in argv[1:]])
    exit(SUCCESS)

if __name__ == "__main__":
    main()
