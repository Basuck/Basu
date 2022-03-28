from op1 import *
l1=[]
l2=[]
op=Operator(l1,l2)
op.getinfo()
op1=Operator(l1,l2)
op2=Operator(l1,l2)
while True:
 print("1.Addition 2.Substraction 3.Multification 4.Division 5.Exit")
 ch=int(input("Enter your Choice"))
 if ch==1:
  op1+op2
 elif ch==2:
  op1-op2
 elif ch==3:
  op1*op2
 elif ch==4:
  op1//op2
 elif ch==5:
  exit()
