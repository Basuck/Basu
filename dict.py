dict = {}
class Employee:
 def getdata(self):
  name = input("Enter Name: ")
  addr = input("Enter Address: ")
  pan = input("Enter Pan Numer: ")
  basic = float(input("Basic Salary: "))
  da = basic*0.2
  hra = basic*0.3
  tds = basic*0.4
  gross = da + hra + basic
  net = gross - da
  dict.update({
  "Name":name,
  "Address":addr,
  "Pan":pan,
  "Basic":basic,
  "DA":da,
  "Hra":hra,
  "Tds":tds,
  "Gross":gross,
  "Net":net
  })

 def search(self,key):
  if key in dict.keys():
   print(dict.get(key))
  else:
   print("Does Not Exist")
 def search(self,items):
  if items in dict.items():
   print(dict.get(items))
  else:
    print("Does Not exist")
 def display(self):
   print("Employee Details")
   print("Name",dict.get("Name"))
   print("Address",dict.get("Address"))
   print("Pan",dict.get("Pan"))
   print("Basic",dict.get("Basic"))
   print("DA",dict.get("DA"))
   print("Hra",dict.get("Hra"))
   print("Tds",dict.get("Tds"))
   print("Gross",dict.get("Gross"))
   print("Net",dict.get("Net"))
emp = Employee()
while True:
 print("1.insert 2.Search key 3.Display 4.exist 5.Search Items")
 ch = input("Enter Choice: ")
 if ch == "1":
  emp.getdata()
 elif ch == "2":
  s = input("Enter key to Search: ")
  emp.search(s)
 elif ch == "3":
  emp.display()
 elif ch == "5":
  t = input("Enter Items to Search: ")
  emp.search(t)
 elif ch == "4":
  exit()
 else:
  print("Invalid Choice")
