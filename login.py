
user = "admin"
passw = 1234
for i in range(1, 4):
    username = input("Enter username: ")
    password = int(input("Enter password: "))
    if (user == username) and (passw == password):
        print("Logged in")
        break
    else:
        print("Try again")


# mlist =[12,21,34,3,222,231]
# for i in mlist:
#     if i%2==0:
#         print(i)
    
# print("completed")