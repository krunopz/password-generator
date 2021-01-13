#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass1=[]
for i in range(0, nr_letters):
  pass1.append(letters[random.randint(0,51)])
for i in range(0, nr_symbols):
  pass1.append(symbols[random.randint(0,8)])
for i in range(0, nr_numbers):
  pass1.append(letters[random.randint(0,9)])
#print(pass1)

password="";
for n in range(0,len(pass1)):
  password=password+pass1[n]
print(f"Easy password : {password}\n")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(pass1);
#print(pass1)
random_password="";
for n in range(0,len(pass1)):
  random_password=random_password+pass1[n];
print(f"Hard password: {random_password}")
print("What is the problem?")