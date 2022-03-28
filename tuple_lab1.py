t1 = ('a','b','c','d','e','f')
t2 = (98,56,43,209,'RVCE')
t3 = (904,345)
print("Enter your choice:/n1:Concatination of tuple /n2:Repetation of tuple /n3:Range of slicing /n4:Slicing of tuple /n5:Length of tuple /n6:MAx of tuple /n7:minimum of tuple /n8:counting of tuple /n9:Membership of tuple /n10:Index of tuple /n11:exit /n")	
while(True):
	ch =int(input("Enter your choice"))
	if(ch==1):
		print("Concatination of tuple:",t1+t2)
	elif(ch==2):
		print("Repetation of tuple:",t1*t2)
	elif(ch==3):
		print("Range of slicing:",t1[0:5])
	elif(ch==4):
		print("Slicing of tuple:",t1[2])
	elif(ch==5):
		print("Length of tuple:",len(t1))
	elif(ch==6):
		print("Maximum of tuple:",max(t1))
	elif(ch==7):
		print("Minimum of tuple:",min(t1))
	elif(ch==8):
		print("Counting of tuple:",t1.count(BASAVANNAYYA))
	elif(ch==9):
		print("Membership of tuple:",'b' in t1)
	elif(ch==10):
		print("Index of tuple:",t1[4][3])
	elif(ch==11):
		break
	else:
		print("Invalid choice")
