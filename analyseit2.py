#!/usr/bin/python

import math

def rotatez(structure):
  newstructure = ""
  for i in range(5):
    if structure[i]=="A":
      newstructure = newstructure + "B"
    if structure[i]=="B":
      newstructure = newstructure + "C"
    if structure[i]=="C":
      newstructure = newstructure + "D"
    if structure[i]=="D":
      newstructure = newstructure + "A"
    if structure[i]=="E":
      newstructure = newstructure + "E"
    if structure[i]=="F":
      newstructure = newstructure + "F"
  return newstructure

def rotatex(structure):
  newstructure = ""
  for i in range(5):
    if structure[i]=="A":
      newstructure = newstructure + "F"
    if structure[i]=="F":
      newstructure = newstructure + "C"
    if structure[i]=="C":
      newstructure = newstructure + "E"
    if structure[i]=="E":
      newstructure = newstructure + "A"
    if structure[i]=="B":
      newstructure = newstructure + "B"
    if structure[i]=="D":
      newstructure = newstructure + "D"
  return newstructure

def rotatey(structure):
  newstructure = ""
  for i in range(5):
    if structure[i]=="B":
      newstructure = newstructure + "E"
    if structure[i]=="E":
      newstructure = newstructure + "D"
    if structure[i]=="D":
      newstructure = newstructure + "F"
    if structure[i]=="F":
      newstructure = newstructure + "B"
    if structure[i]=="A":
      newstructure = newstructure + "A"
    if structure[i]=="C":
      newstructure = newstructure + "C"
  return newstructure

def flip(structure):
  newstructure = ""
  for i in range(5):
    if structure[i]=="E":
      newstructure = newstructure + "F"
    elif structure[i]=="F":
      newstructure = newstructure + "E"
    else:
      newstructure = newstructure + structure[i]
  return newstructure

def findbest(structure):
  if structure[0] in ["B","C","D"]:
    while structure[0]!="A":
      structure = rotatez(structure)
  if structure[0] in ["E","F"]:
    while structure[0]!="A":
      structure = rotatex(structure)
  if structure[1] in ["D","E","F"]:
    while structure[1]!="B":
      structure = rotatey(structure)
  elif structure[2] in ["D","E","F"]:
    while structure[2]!="B":
      structure = rotatey(structure)
  elif structure[3] in ["D","E","F"]:
    while structure[3]!="B":
      structure = rotatey(structure)
  elif structure[4] in ["D","E","F"]:
    while structure[4]!="B":
      structure = rotatey(structure)
  return structure

hit = 0.0
tot = 0.0
ifile = open("mc1kT.txt", "r").readlines()
for line in ifile:
  best = findbest(line[:-1])
  best2 = findbest(flip(line[:-1]))
  if best == "ABECF":
    hit = hit + 1.0
  if best2 == "ABECF":
    hit = hit + 1.0
  tot = tot + 1.0
  print tot, 100.0*hit/tot

