class Operator :
 def __init__(self):
  self.list=[]
 def getelement(self):
  self.n=int(input("Enter maximum number: "))
  for i in range(self.n):
   self.list.append(int(input("Enter element: ")))
  print(self.list)
 def __add__(self,others):
  self.nl=[]
  self.zl=zip(self.list,others.list)
  for i in self.zl:
   self.nl.append(i[0]+i[1])
  print(self.nl)
 def __sub__(self,others):
  self.nl=[]
  self.zl=zip(self.list,others.list)
  for i in self.zl: 
   self.nl.append(i[0]-i[1])
  print(self.nl)
 def __mul__(self,others):
  self.nl=[]
  self.zl=zip(self.list,others.list)
  for i in self.zl: 
   self.nl.append(i[0]*i[1])
  print(self.nl)
 def __floordiv__(self,others):
  self.nl=[]
  self.zl=zip(self.list,others.list)
  for i in self.zl: 
   self.nl.append(i[0]//i[1])
  print(self.nl)
from inheritance import *
ov1=Operator()
ov2=Operator()
while True:
 ov1.getelement()
 ov2.getelement()
 ov1+ov2
 ov1-ov2
 ov1*ov2
 ov1//ov2
