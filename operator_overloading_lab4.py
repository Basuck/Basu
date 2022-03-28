class Operator :
 def __init__(self,l1,l2):
  self.l1=l1
  self.l2=l2
 def getinfo(self):
   n=int(input("Enter how many Element you want to add to the list :"))
   for i in range(n):
    ele1=int(input("Enter list1 Element:"))
    self.l1.append(ele1)
   print(self.l1)
   for i in range(n):
    ele2=int(input("Enter List2 element:"))
    self.l2.append(ele2)
   print(self.l2)
 def __add__(self,others):
  a=[]
  n=len(self.l1)
  for i in range(n):
   a.append(self.l1[i]+others.l2[i])
  print(a) 
 def __sub__(self,others):
  a=[]
  n=len(self.l1)
  for i in range(n): 
   a.append(self.l1[i]-others.l2[i]) 
  print(a) 
 def __mul__(self,others):
  a=[]
  n=len(self.l1)
  for i in range(n): 
   a.append(self.l1[i]*others.l2[i]) 
  print(a) 
 def __floordiv__(self,others):
  a=[]
  n=len(self.l1)
  for i in range(n): 
   a.append(self.l1[i]//others.l2[i]) 
  print(a) 

