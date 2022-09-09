#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from generationMonstre import *
import random

def createMonster():
    liste_monstres=["Vathana", "Yacime", "Martin"]
    nameMonster=random.choice(liste_monstres)
    return degatMonstre(nameMonster)