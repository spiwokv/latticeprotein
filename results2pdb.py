#!/usr/bin/python

def abcd2pdb(abcd):
  ofilename = abcd+".pdb"
  ofile = open(ofilename, "w")
  x = []
  y = []
  z = []
  for i in range(len(abcd)+1):
    x.append(0.0)
    y.append(0.0)
    z.append(0.0)
  print abcd
  for i in range(len(abcd)):
    if abcd[i]=="A":
      for j in range(i,len(abcd)):
        y[j+1] = y[j+1] - 1.4
    if abcd[i]=="B":
      for j in range(i,len(abcd)):
        x[j+1] = x[j+1] + 1.4
    if abcd[i]=="C":
      for j in range(i,len(abcd)):
        y[j+1] = y[j+1] + 1.4
    if abcd[i]=="D":
      for j in range(i,len(abcd)):
        x[j+1] = x[j+1] - 1.4
    if abcd[i]=="E":
      for j in range(i,len(abcd)):
        z[j+1] = z[j+1] + 1.4
    if abcd[i]=="F":
      for j in range(i,len(abcd)):
        z[j+1] = z[j+1] - 1.4
  #        P S V K M A
  ofile.write("ATOM      1  CA  PRO     1    %8.3f%8.3f%8.3f\n" % (x[0],y[0],z[0]))
  ofile.write("ATOM      2  CA  SER     2    %8.3f%8.3f%8.3f\n" % (x[1],y[1],z[1]))
  ofile.write("ATOM      3  CA  VAL     3    %8.3f%8.3f%8.3f\n" % (x[2],y[2],z[2]))
  ofile.write("ATOM      4  CA  LYS     4    %8.3f%8.3f%8.3f\n" % (x[3],y[3],z[3]))
  ofile.write("ATOM      5  CA  MET     5    %8.3f%8.3f%8.3f\n" % (x[4],y[4],z[4]))
  ofile.write("ATOM      6  CA  ALA     6    %8.3f%8.3f%8.3f\n" % (x[5],y[5],z[5]))


ifile = open("mc1kTresults.txt","r").readlines()

data = []
for line in ifile:
  sline = str.split(line)
  data.append((int(sline[1]), sline[0][2:-1]))
data = sorted(data, key=lambda data1: data1[0])

for i in range(20):
  abcd2pdb(data[-i-1][1])
