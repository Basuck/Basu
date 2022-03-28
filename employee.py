employee = {
"NAME":"BASU",
"Address":"Bangalore",
"PAN":"GRIPK090K",
"BASIC":35000,
"TDS":2000,
"DETUCT":5000,
"HRA":980,
"DA":1900
}
print(employee)
print(" Gross salary")
a = employee["BASIC"]
b = employee["HRA"]
c  = employee["DA"]
y = employee["DETUCT"]
x = "grosssalary"
grosssalary = a+b+c
print(grosssalary)
z = "netsalary"
netsalary = y
print("netsalary")
f = "dedaction"
dedaction = y
netsalary =grosssalary - dedaction
print(netsalary)
print("Update the employee details")
employee["ID"] = 567
print(employee)
print("Search the values")
print(employee["DA"])
print("Employee Details")
for x,y in employee.items():
 print(x,y)
