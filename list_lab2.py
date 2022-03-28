list1=['a','b','c','d','e']
list2=[3,404,'mca']
list3=[8]
print("Enter your choice:/n1:Creating list /n2:Concatination list /n3:Repetation List /n4:Rang of slicing list /n5:Slicing list /n6:List Membership /n7:Minimum List /n8:Length of List /n9:Maximum Value /n10:Reversing List")
while(True):
        ch =int(input("Enter your choice: "))
        if(ch==1):
                print("Creating List:",['RVCE'])
        elif(ch==2):
                print("Concatination List:",list1+list2)
        elif(ch==3):
                print("Repetation List:",list2*2)
        elif(ch==4):
                print("Range of Slicing List:",list1[0:3])
        elif(ch==5):
                print("Slicing List:",list1[1])
        elif(ch==6):
                print("List Membership:",'H' in list1)
        elif(ch==7):
                print("Minimum List:",min(list1))
        elif(ch==8):
                print("Length of List:",len(list1))
        elif(ch==9):
                print("Maximum Value in List:",max(list1))
        elif(ch==10):
                print("Reversing List:",list1[::-1])
        elif(ch==11):
                break
        else:
                print("Invalid choice")
