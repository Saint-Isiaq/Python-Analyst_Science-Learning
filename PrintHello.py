#Escape Sequences
print("\n\t----------------")
print('\tBonjour le monde')
print("\t----------------\n\n")
print("Path: C:\\Users\\Saint\n")
print("Message 1\n")
print("message 2\n")
#case 2
print("messenger 1\tmessage 1\tmessage 2\n")  #Just testing out Escape Sequences
#Case 3
print('\tMaths Examen\n')
print("\tEq--1.x-y+2=4\n\tEq--2.x+2y-2=6\tTrouve le X et Y")

#Print Challenge
print()  
print("""Your learning path:
\t-python basics
\t-Data science
\t-AI\n""") #I got it

# Variables
Language = "C++ & python"
print("My name is Saint")
print("Saint is Learning",Language)
print("Saint wants to become",Language,"expert\n")
#Case 2
name = "miralet"
print("My name is", name)
print(name, "is Learning",Language)
print(name, "wants to become",Language,"expert")

#python Challenge(Variables)
email = "@datawithbaraa"
name = "datawithbaraa"
print("info",email,".com\nsupport",email,".com\nwww.",name,".com") #I got it, hehehe

#input Function
name = input("What is your name?") #Needs an input
country = "Canada"  #Hardcoded value ;Displays with user input
print("Ohh!,you are",name,"\nWelcome to",country)
#Python Challenge
ask = input("Quelle est ton nom?")
place = input("etes-vien ou?")
cars = input("What cars do you like?")
print('\n-------------Expo-----------------')
print("\n:Hey there,",ask,
       "\n;-je voir!,vous-etes vien",place,
       "\n;-Ohh!,tu connais",cars,
       "\n;-Great Taste in cars!,my bruv")
print("------------------------------------")

#Data types
a = 10 #int
b = 3.17 #float
c = "Hello" #str
d = 'hey'  #str
e = "1234" #str
f = True   #boolean
g = False  #bool
h = None   #none
i = ""     #str - blank
j = " "    #str - white space

text = "hey"
number = 15

print(len(text))
print(text.upper())
print(number.bit_length())

#python challenge (Data types)
age = 22
height = 6.0
name = "saint"
student = True
status = ""

print("my age is",age)
print('i am',height,'Feet')
print("my name is",name)
print('i am a student, right?:',student)
print("Am i married?",status)
print()
print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(status))

#types Fx
name = "saint"
age = 22
print(type(name))#lets us know type of data class
print("your age is:" + str(age)) #Changes Int to String while using operation(+,-,/: with a str value)
# age = str(age)
print(type(age)) 

#Math fx
passcode = '23345'
print(len(passcode))
if len(passcode) < 7:
   print("write better passcode dude;if not?")
   #len:used to validate length ,prevent values that are too long or short.

#Count(substring) :this returns how many times a word appears in the str
word = """ 
python is a fun case,
Will it be difficult?,no i have a cool python teacher
python with baraa is cool to do.
"""
print(word.count('python'))  #uses:detect quality issues in data, count 
#how many unwanted characters in the code 

#Transformations fx
number = "123,56"
print(number.replace(",","."))
#case 2
phonenumber = '816/500/7123'
#print(phonenumber.replace("/","-")) #or
print(phonenumber.replace("/",""))
#case 3
price = "$4,756.98"
print(price.replace("$","").replace(",",""))

#python challenge
phonnumb = "+49 (176) 123-4567"
print(phonnumb.replace("+","00").
      replace("(","").
         replace(")","").
             replace(" ","").
                 replace("-",""))#got it: sweet

#concatenations =joining multiple strings together
first_name = "Saint"
last_name = "Isiaq"
prenom = first_name+"-"+last_name
print(prenom)
#F{string}
name = 'Ader'
age = 24
stud_stat = True
print("my name is " + name,
      ",i am "+str(age),
      "and my student status is "+str(stud_stat)
      ,".")#prev way to do this before f{}, now
print(f"""My name is {name} ,i am {age} and my student status is {stud_stat}.
      """) #done with f{}, neat.
print(f"54+23 = {54 + 23}") #f{can also be used for int expressions}
#split
Stamp = "2025-08-19 14:30"
print(Stamp.split(" ")) 
#Case 2
stamps = "2026-06-23"
print(stamps.split("-"))
#Multiplier
print('='*10)
print("ha" * 3)#hahaha, lol
print('#'*10)
#Indexing and Slicing
#Index case
text = "Science"
print(text[1]), print(text[-4]), print(text[0])
#Slicing
dat = '2026-07-23'
print(dat[:-6]),print(dat[5:7]), 
print(dat[-2:]),print(dat[0:]) 

#Cleaning #cleaning white spaces
#l.strip #left-strip
text = " python".lstrip() #case 1
print(text)
#r.strip #right-strip
text = "python ".rstrip()
print(text)
#strip() #to check data quality, check length before strip and strip.
text = "  python  "
print(len(text))
print(len(text.strip()))

no_of_spaces = len(text) - len(text.strip())
str_Quality = len(text) == len(text.strip())
print("How many space:",no_of_spaces)
print("is my data quality?:",str_Quality)


#Case 2 for .strip()
text = "Data analytics".strip() #doesn't work for in-line spaces
print(text)
#case 3 for .strip()
texp = "$$$qwerty$$$".strip("$")
print(texp)

#case conversion 
#lower
text = "pYthon"
print(text.lower())
#upper
search = "Gmail ".lower().strip()
data = "gmaIl".lower().strip()
print(search == data)
# case 2
teft = "Should".upper()
print(teft)

#python challenge:turn messy str into clean summary:name,role,age
Data = "968-Maria, ( Data Engineer );; 27y  ".replace("968-","name:").replace(",","").replace("(","role:").replace(")","").replace(";;","age:").replace("y","").strip().lower()

print(Data)  #Got it?, i sure did, lol

#Searching fx
#startswith
phone = "+234-123-234-656"
print('is this a nigerian number?:',phone.startswith("+234"))
#endswith
Emale = "Saint@gmail.com"
print('Is my address gmail.com?:',Emale.endswith("gmail.com"))
#case2
file = "data_backing.csv"
print("Cet file est un csv?:",file.endswith('.csv'))
#in -an operator
print(".csv"in file)
#case 2
Emale = "Saint@gmail.com"
print("This email is valid?:","@"in Emale)
#case 3
web = "https://api.company.com/Az/data"
print("does this site have an api call?", "/api"in web)
#find
phone1 = "+35-556-56876"
phone2 = "35-665-65768"
phone3 = "0035-666-65768"
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

print(phone1.find("-")) #find(string)

#Validations fx
#isalpha # validates if str contains only alphabets
country = "Canada"
print(country.isalpha())

#isnumeric #validates if str contains only numbers
phone = "34566789.2"
print(phone.isnumeric())

###################################################################

#Working with numberss.
#type fx
x = 3
y = 3.87
z = 3.6j
print(type(x))
print(type(y))
print(type(z))

#int
x = 3.56
print(int(x))
#case 2
x = "23"
print(int(x))
#float
x = 56
print(float(x))
#case 2
y = "34"
print(float(y))
#complex
x = 4 #real part
y = 65 #imaginary part
print(complex(x,y)) 
# case 2
x = '56'
y = 3
print(complex(x,y)) #doesn't work, all arguments must be values

#math operators
print(4+3) # (+) sign
print(5-3) # (-) sign
print(4*7) # (*) sign
print(20/7)  # (/) sign
print(20//7) # (//) sign #returns whole no of divided no
print(9 % 6) # (%) sign  #returns a remainder of divided value
print(4**3)  # (**) sign #multiplies original value by int at the end

 #case 2
x = 10
#x = x * 8
 #instead of this now, i'll be trying that
x **= 8  #easier
print (x) #much neater this way(a lil bit understanding)


#ROUNDING fx
import math
#round
price = 45.645679
print(round(price))  #nearest whole number
#case 2
print(round(price,2))  #rounds to the nearest decimals
#floor
print(math.floor(price)) #lowest rounding
#ceil
print(math.ceil(price))  #highest rounding
#trunc
print(math.trunc(price))  #removes all decimal values
#abs()  
x = 5 - 7
print(abs(x))  #absolves negativity ,returns positive

#Random fx
import random
print(f"""this prints, [{random.random()}] floats at random:
      """) 
#Randint
print(f"""\nthis prints, [{random.randint(1,100)}] int in range 100"
      """)
#case 2
print(f"""\nthis prints, [{random.randint(2,300)}] int in range 2,300
      """)

#Validations
#is_integer
x = 43.6
print(x.is_integer())
#case 2
y = 66.0
print(y.is_integer())
#isinstance
x = 66.5
print(isinstance(x,str))
#case 2
y = 77.0
print(isinstance(y,int))

#python challenge
#generate a random int btw 1 nd 100, then check if the output is even
import random
print(random.randint(1,100)//random.randint(1,100)) #Got it


