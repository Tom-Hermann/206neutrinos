##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-206neutrinos-tom.hermann
## File description:
## calcul
##

from math import sqrt

def calcul_AMean(nb_value, new, Amean):
    return Amean + (new - Amean) / nb_value

def calcul_HMean(nb_value, new, Hmean):
    return 1 / ((1 / Hmean) + ((1 / new) - (1 / Hmean)) / nb_value)

def calcul_QMean(nb_value, new, Amean, Sd):
    return sqrt(((Sd ** 2 + Amean ** 2) * (nb_value - 1) + new ** 2) / nb_value)

def calcul_Sd(nb_value, new, Sd, mean, save):
    res = ((nb_value - 2) * Sd ** 2) + (new - mean) * (new - save)
    return sqrt(res / (nb_value - 1))