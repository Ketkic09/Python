def get_detail():
    f1= open("C:\\Users\\ketki\\Assignments\\assgn1\\contact2.txt","a")
    name = input("Enter name number nunber,email: ")
    f1.write(name+"\n")
    print(name)
    f1.close
def search():
    f2 = open("C:\\Users\\ketki\\Assignments\\assgn1\\contact2.txt","r")
    s = input("Enter name/no./email ")
    d = 0
      
    for k in f2:
        text = f2.readline().strip().split()
        for i in text :
           
            if i== '':
                continue 
            elif i in s :
                d+=1
                break 
        
            else:
               pass
        if d > 0:
            print("found")
            print(text)
            break
        
    f2.close

x = 0
while x!=3:
    print("Enter 1 to get details  2 to search  3 to exit")
    x = int(input("Enter choice "))
    if x == 1:
        get_detail()
    elif x==2:
        search()
    elif x>3:
        
        print("Invalid")