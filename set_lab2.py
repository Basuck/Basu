set1={1,2,3,4,5,6}
set2={10,9,8,7,6,5}
set3={'mca','mtech','BCA'}
print("Enter your choice:/n1 Size in bytes/n2 Lenth/n3 Adding new value/n4 POP/n5 Insertation/n6 Set Difference/n7 Symmetric Difference/n8 Element in set/n9 Clearing set/n10 Deleting Set ")
while(True):
        ch =int(input("Enter your choice: "))
        if(ch==1):
                print("Size in bytes Set1:",set1.__sizeof__())
        elif(ch==2):
                print("Length os set1:",len(set1))
        elif(ch==3):
            print("Adding New Value in set2:",set2.add(7))
        elif(ch==4):
            print("PoP in set2:",set2.pop())
        elif(ch==5):
            print("Intersection:",set1.intersection(set2))
        elif(ch==6):
            print("Set Difference:",set1-set2)
        elif(ch==7):
            print("Symmetric Difference:",set1^set2)
        elif(ch==8):
            print("Elemenet in set3:",set3.__contains__(8))
        elif(ch==9):
            print("Clearing Set3:",set3.clear())
        elif(ch==10):
            print("Union Element in Set1 And set2:",set1.union(set2))
        elif(ch==11):
                break
        else:
                print("Invalid choice")
