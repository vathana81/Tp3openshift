# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:16:12 2022

@author: Administrateur
"""

from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__)

import sys
import os
import cptr, createMonster, creationPerso, degats, generationMonstre, gestioncombat
global perso
perso = []

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.form:
        compteurKill=0
        listeMonstresPerdus=[]
        global pseudo
        pseudo=request.form["name"]
        #je récupère le name dans mon input html
        monPerso=perso(pseudo,15,6,1)
        
        while monPerso[1] > 0:
            nameMonster=createMonster()
            gestioncombat(monPerso, nameMonster)
            
            if monPerso[1] > 0:
                compteurKill+=1
                listeMonstresPerdus.append(nameMonster[0])
                
        return render_template("home.html", pseudo-pseudo, compteurKill-compteurKill, listeMonstresPerdus-listeMonstresPerdus)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)