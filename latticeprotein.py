#!/usr/bin/python

import math, random

T = 1.0

aa = ["C", "M", "F", "I", "L", "V", "W", "Y", "A", "G", "T", "S", "N", "Q", "D", "E", "H", "R", "K", "P"]

#           Cys,   Met,   Phe,   Ile,   Leu,   Val,   Trp,   Tyr,   Ala,   Gly,   Thr,   Ser,   Asn,   Gln,   Asp,   Glu,   His,   Arg,   Lys,   Pro
imat = [[ -5.44, -4.99, -5.80, -5.50, -5.83, -4.96, -4.95, -4.16, -3.57, -3.16, -3.11, -2.86, -2.59, -2.85, -2.41, -2.27, -3.60, -2.57, -1.95, -3.07], # Cys
        [ -4.99, -5.46, -6.56, -6.02, -6.41, -5.32, -5.55, -4.91, -3.94, -3.39, -3.51, -3.03, -2.95, -3.30, -2.57, -2.89, -3.98, -3.12, -2.48, -3.45], # Met
        [ -5.80, -6.56, -7.26, -6.84, -7.28, -6.29, -6.16, -5.66, -4.81, -4.13, -4.28, -4.02, -3.75, -4.10, -3.48, -3.56, -4.77, -3.98, -3.36, -4.25], # Phe
        [ -5.50, -6.02, -6.84, -6.54, -7.04, -6.05, -5.78, -5.25, -4.58, -3.78, -4.03, -3.52, -3.24, -3.67, -3.17, -3.27, -4.14, -3.63, -3.01, -3.76], # Ile
        [ -5.83, -6.41, -7.28, -7.04, -7.37, -6.48, -6.14, -5.67, -4.91, -4.16, -4.34, -3.92, -3.74, -4.04, -3.40, -3.59, -4.54, -4.03, -3.37, -4.20], # Leu
        [ -4.96, -5.32, -6.29, -6.05, -6.48, -5.52, -5.18, -4.62, -4.04, -3.38, -3.46, -3.05, -2.83, -3.07, -2.48, -2.67, -3.58, -3.07, -2.49, -3.32], # Val
        [ -4.95, -5.55, -6.16, -5.78, -6.14, -5.18, -5.06, -4.66, -3.82, -3.42, -3.22, -2.99, -3.07, -3.11, -2.84, -2.99, -3.98, -3.41, -2.69, -3.73], # Trp
        [ -4.16, -4.91, -5.66, -5.25, -5.67, -4.62, -4.66, -4.17, -3.36, -3.01, -3.01, -2.78, -2.76, -2.97, -2.76, -2.79, -3.52, -3.16, -2.60, -3.19], # Tyr
        [ -3.57, -3.94, -4.81, -4.58, -4.91, -4.04, -3.82, -3.36, -2.72, -2.31, -2.32, -2.01, -1.84, -1.89, -1.70, -1.51, -2.41, -1.83, -1.31, -2.03], # Ala
        [ -3.16, -3.39, -4.13, -3.78, -4.16, -3.38, -3.42, -3.01, -2.31, -2.24, -2.08, -1.82, -1.74, -1.66, -1.59, -1.22, -2.15, -1.72, -1.15, -1.87], # Gly
        [ -3.11, -3.51, -4.28, -4.03, -4.34, -3.46, -3.22, -3.01, -2.32, -2.08, -2.12, -1.96, -1.88, -1.90, -1.80, -1.74, -2.42, -1.90, -1.31, -1.90], # Thr
        [ -2.86, -3.03, -4.02, -3.52, -3.92, -3.05, -2.99, -2.78, -2.01, -1.82, -1.96, -1.67, -1.58, -1.49, -1.63, -1.48, -2.11, -1.62, -1.05, -1.57], # Ser
        [ -2.59, -2.95, -3.75, -3.24, -3.74, -2.83, -3.07, -2.76, -1.84, -1.74, -1.88, -1.58, -1.68, -1.71, -1.68, -1.51, -2.08, -1.64, -1.21, -1.53], # Asn
        [ -2.85, -3.30, -4.10, -3.67, -4.04, -3.07, -3.11, -2.97, -1.89, -1.66, -1.90, -1.49, -1.71, -1.54, -1.46, -1.42, -1.98, -1.80, -1.29, -1.73], # Gln
        [ -2.41, -2.57, -3.48, -3.17, -3.40, -2.48, -2.84, -2.76, -1.70, -1.59, -1.80, -1.63, -1.68, -1.46, -1.21, -1.02, -2.32, -2.29, -1.68, -1.33], # Asp
        [ -2.27, -2.89, -3.56, -3.27, -3.59, -2.67, -2.99, -2.79, -1.51, -1.22, -1.74, -1.48, -1.51, -1.42, -1.02, -0.91, -2.15, -2.27, -1.80, -1.26], # Glu
        [ -3.60, -3.98, -4.77, -4.14, -4.54, -3.58, -3.98, -3.52, -2.41, -2.15, -2.42, -2.11, -2.08, -1.98, -2.32, -2.15, -3.05, -2.16, -1.35, -2.25], # His
        [ -2.57, -3.12, -3.98, -3.63, -4.03, -3.07, -3.41, -3.16, -1.83, -1.72, -1.90, -1.62, -1.64, -1.80, -2.29, -2.27, -2.16, -1.55, -0.59, -1.70], # Arg
        [ -1.95, -2.48, -3.36, -3.01, -3.37, -2.49, -2.69, -2.60, -1.31, -1.15, -1.31, -1.05, -1.21, -1.29, -1.68, -1.80, -1.35, -0.59, -0.12, -0.97], # Lys
        [ -3.07, -3.45, -4.25, -3.76, -4.20, -3.32, -3.73, -3.19, -2.03, -1.87, -1.90, -1.57, -1.53, -1.73, -1.33, -1.26, -2.25, -1.70, -0.97, -1.75]] # Pro



seq = "PSVKMA"

#        P S V K M A
#imat = [[0,0,0,1,0,2], #P
#        [0,0,0,0,3,0], #S
#        [0,0,0,0,0,4], #V
#        [1,0,0,0,0,0], #K
#        [0,3,0,0,0,0], #M
#        [2,0,4,0,0,0]] #A


def energy(structure):
  x = []
  y = []
  z = []
  for i in range(len(structure)+1):
    x.append(0)
    y.append(0)
    z.append(0)
  for i in range(len(structure)):
    if structure[i]=="A":
      for j in range(i,len(structure)):
        y[j+1] = y[j+1] - 1
    if structure[i]=="B":
      for j in range(i,len(structure)):
        x[j+1] = x[j+1] + 1
    if structure[i]=="C":
      for j in range(i,len(structure)):
        y[j+1] = y[j+1] + 1
    if structure[i]=="D":
      for j in range(i,len(structure)):
        x[j+1] = x[j+1] - 1
    if structure[i]=="E":
      for j in range(i,len(structure)):
        z[j+1] = z[j+1] + 1
    if structure[i]=="F":
      for j in range(i,len(structure)):
        z[j+1] = z[j+1] - 1
  energy = 0
  for i in range(len(structure)+1):
    for j in range(i+1,len(structure)+1):
      if abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j])==1:
        energy = energy + imat[aa.index(seq[i])][aa.index(seq[j])]
      if abs(x[i]-x[j])+abs(y[i]-y[j])+abs(z[i]-z[j])==0:
        energy = energy + 10000000.0
        break
  return energy

def changeit(structure):
  #End moves
  if random.random()<0.5:
    r = random.randrange(6)
    if r==0:
      structure = "A" + structure[1:]
    if r==1:
      structure = "B" + structure[1:]
    if r==2:
      structure = "C" + structure[1:]
    if r==3:
      structure = "D" + structure[1:]
    if r==4:
      structure = "E" + structure[1:]
    if r==5:
      structure = "F" + structure[1:]
  if random.random()<0.5:
    r = random.randrange(6)
    if r==0:
      structure = structure[:-1] + "A"
    if r==1:
      structure = structure[:-1] + "B"
    if r==2:
      structure = structure[:-1] + "C"
    if r==3:
      structure = structure[:-1] + "D"
    if r==4:
      structure = structure[:-1] + "E"
    if r==5:
      structure = structure[:-1] + "F"
    #Corner moves
  for i in range(len(structure)-1):
    part1 = structure[i]
    part2 = structure[i+1]
    if (part1=="A" or part1=="C") and (part2=="B" or part2=="D"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
    if (part1=="B" or part1=="D") and (part2=="A" or part2=="B"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
    if (part1=="B" or part1=="D") and (part2=="E" or part2=="F"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
    if (part1=="E" or part1=="F") and (part2=="B" or part2=="D"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
    if (part1=="A" or part1=="C") and (part2=="E" or part2=="F"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
    if (part1=="E" or part1=="F") and (part2=="A" or part2=="B"):
      if random.random()<0.5:
        structure = structure[:i]+part2+part1+structure[i+2:]
  #Crankshaft moves
  for i in range(len(structure)-2):
    part1 = structure[i]
    part2 = structure[i+1]
    part3 = structure[i+2]
    if ((part1=="A" and part3=="C") or (part1=="C" and part3=="A")) and (part2=="B" or part2=="D"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"A"+part2+"C"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"C"+part2+"A"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"E"+part2+"F"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"F"+part2+"E"+structure[i+3:]
    if ((part1=="A" and part3=="C") or (part1=="C" and part3=="A")) and (part2=="E" or part2=="F"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"A"+part2+"C"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"C"+part2+"A"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"B"+part2+"D"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"D"+part2+"B"+structure[i+3:]
    if ((part1=="B" and part3=="D") or (part1=="D" and part3=="B")) and (part2=="A" or part2=="C"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"B"+part2+"D"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"D"+part2+"B"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"E"+part2+"F"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"F"+part2+"E"+structure[i+3:]
        structure = structure[:i]+part3+part2+part1+structure[i+3:]
    if ((part1=="B" and part3=="D") or (part1=="D" and part3=="B")) and (part2=="E" or part2=="F"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"B"+part2+"D"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"D"+part2+"B"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"A"+part2+"C"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"C"+part2+"A"+structure[i+3:]
        structure = structure[:i]+part3+part2+part1+structure[i+3:]
    if ((part1=="E" and part3=="F") or (part1=="F" and part3=="E")) and (part2=="A" or part2=="C"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"E"+part2+"F"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"F"+part2+"E"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"B"+part2+"D"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"D"+part2+"B"+structure[i+3:]
        structure = structure[:i]+part3+part2+part1+structure[i+3:]
    if ((part1=="E" and part3=="F") or (part1=="F" and part3=="E")) and (part2=="B" or part2=="D"):
      if random.random()<0.5:
        r = random.randrange(4)
        if r==0:
          structure = structure[:i]+"E"+part2+"F"+structure[i+3:]
        if r==1:
          structure = structure[:i]+"F"+part2+"E"+structure[i+3:]
        if r==2:
          structure = structure[:i]+"A"+part2+"C"+structure[i+3:]
        if r==3:
          structure = structure[:i]+"C"+part2+"A"+structure[i+3:]
        structure = structure[:i]+part3+part2+part1+structure[i+3:]
  return structure

structure = "AAAAA"

for i in range(1000000):
  newstructure = changeit(structure)
  e = energy(structure)
  newe = energy(newstructure)
  if newe<e:
    structure = newstructure
  else:
    metro = math.exp((e-newe)/T)
    #print metro
    if random.random() < metro:
      structure = newstructure
  print structure

