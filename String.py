str1="rv collage of engineering"
str2="mca first sem student"
str3="PYTHON"
print("Enter your choice:/n1:Concatination of String /n2:Repetation of String /n3:Range of slicing /n4:Slicing of String /n5:Length of String /n6:MAx of ")
while(True):
        ch =int(input("Enter your choice: "))
        if(ch==1):
                print("Concatination of string:",str1+str2)
        elif(ch==2):
                print("Repetation of String:",str1*2)
        elif(ch==3):
                print("Range of slicing:",str1[::-1])
        elif(ch==4):
                print("Slicing of String:",str1[0:6])
        elif(ch==5):
                print("Length of String:",len(str1))
        elif(ch==6):
                print("Maximum of String:",max(str1))
        elif(ch==7):
                print("Minimum of String:",min(str1))
        elif(ch==8):
                print("Counting of String:",str1.count("engineering"))
        elif(ch==9):
                print("Membership of String:",'e' in str1)
        elif(ch==10):
                print("Index of String:",str1[7])
        elif(ch==11):
                break
        else:
                print("Invalid choice")


