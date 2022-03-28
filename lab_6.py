from multipledispatch import dispatch
class over:
 @dispatch (int,int)
 def product(n1,n2):
  result=n1*n2
  print(result)
 @dispatch(float,float)
 def product(n1,n2):
  result=n1*n2
  print(result)

 product(8,9)
 product(7.89,5.67)
