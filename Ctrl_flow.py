fame = "je suis apprend python"
print(f"""hello world, {fame} et il est amusant""")

#Boolean Expressions
print(True), print(False), print(type(True)), print(True)
print(bool(567)), print(bool('hey')), print(bool())
print(bool(0)), print(bool('')), print(bool(None))

#value operators which returns boolean
print(3 >= 7), print(3 <= 7), print(3-5 != 7), 
print(len("hello") == 7)
print('a' == 'a'), print('A' == 'a')

#chained Comparisons
print(3 <= 7 >= 6), print(3 <= 7 >= 9)
#case 2
# Is age between 18 and 32
age = 24
print(18 <= age <= 32)

#Any and All
#Any
email = ""
phone = "81670052"
username = 'saint@gmail'
print(any([email,phone,username]))
#case 2  #All
print(all([email,phone,username]))

#logical operators  #and #or #not
#And  #both must be true
print(3>2 and 4>1)
#case 2
print(6>4 and 1>2)
#All  #atleast one must be true
print(4==4 or 3==2)
#case 2
print(4>3 or 5!=5)
#Or
 # Use case (real) #checks if d system is under pressure
cpu_usage = 75
memory_usage = 90
print(cpu_usage > 90 or memory_usage >90)
#case 3 #checking if credentials are true
email = True
password = False
print(email and password)
#Not
print(not False), print(not __name__), print(not 0)
print(not "")

#execution order 
print(5==5 or 3>5 and 6<7)
#case 2
print((5==4 or 3>5) and 6<7)

#Python Task  #Allow access only if User is logged in ,
                #or they are a guest, but they must not be banned
logged_in = True
guest = False
not_banned = True
print(logged_in or guest and not_banned)

#Membership Operators  #in #not-in
print("s" in "saint")
#case 2
list = ["saint","habeeb","jumai"]
print("beejay" in list)
#not-in
print("beejay" not in list)
#case 2
print("habeeb" not in list)

#identity operators #is #is-not
x = [2,3,4,6]
y = [2,3,4,6]
print(x is y)
#case 2
x = [4,3,2,1]
y = x
print(x is y)
#case 3
x = 373
y = 373
print(x is y)
                    #is-not
x = [2,3,4,6]
y = [2,3,4,6]
print(x is not y)
#case 2 Task
email = "saint@"
print(email != None and email != "")

#python challenges
#1
email = "sport@gmail"
age = "17"
print(email != "" and age >= "18") #checked
#2
password = " rtew32489".strip()
print(9 != password and password != " ")
#3
email = "try@.com"
print( "@" in email and ".com" in email and email != "")
#4
username = "saint"
print((username == str and username != None) and username != 6)
#5
user = "moderator"
status = "not-banned"
email = "not-verified"
print(user == "admin" or "moderator" and 
      status == "not_banned" 
      and email == "verified") #logical operators end
#

#Conditional statements #if #else #elif
#if
score = 40
if score >= 90:
    print("A")
#case 2
score = 95
if score >= 90:
    print("A")

#else
score = 95
if score >= 90:
    print("A: Excellent")
else:
    print("D")
#case 2
score = 89
if score >= 90:
    print("A: Excellent")
else:
    print("D: Try better")

#elif
score = 89
if score >= 90:
    print("A: Excellent")
elif score >= 70:
    print("B: Very good")
else:
    print("D: Try better")

#case 2 branching #elif
#elif
score = 46
if score >= 90:
    print("A: Excellent")
elif score >= 70:
    print("B: Very good")
elif score >= 51:
    print("C: Good")
elif score >= 41:
    print("D: Sit-up")
else:
    print("F: Try again")

#nested IF
score = 96
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+: Wonderful")
    else:
        print("A: Excellent")
elif score >= 70:
    print("B: Very good")
elif score >= 51:
    print("C: Good")
elif score >= 41:
    print("D: Sit-up")
else:
    print("F: Try again")

#Connecting condition statement avec #et  #ou
score = 40
submitted_project = True
if score >= 90 and submitted_project:
    print("A+: Wonderful")
elif score >= 70:
    print("B: Very good")
elif score >= 51:
    print("C: Good")
elif score >= 41 or submitted_project:
    print("D: Sit-up")
else:
    print("F: Try again")
    
#Independent IFs
score = 72
submitted_project = True
if score >= 90 and submitted_project:
    print("A+: Wonderful")
elif score >= 80 or submitted_project:
    print("B: you can improve")
else:
    print("A: Good")
if submitted_project:
    print("Status: project submitted")
else:
    print("Status: project needs to be submitted_project")

#Inline IFs
score = 92
submitted_project = True
print("A+: Wonderful" if score >= 90 or submitted_project 
      else "B: you can improve" 
      if score >= 80 or submitted_project else 
      "C: do better")
#case 2
score = 92
submitted_project = True
performance_status = ("A+: Wonderful" if score >= 90 or submitted_project 
      else "B: you can improve" 
      if score >= 80 or submitted_project else 
      "C: do better")
print(performance_status)

#Match case Task #country's abbreviation
country = "9ja"
match country:
    case  "Nigeria":
        print("Ng")
    case "United states":
        print("US")
    case "France":
        print("Fr")
    case "Germany":
        print("De")
    case _:
        print("Unknown")
#case 2
country = "USA"
match country:
    case  "Nigeria" | "9ja":
        print("Ng")
    case "United states" | "USA":
        print("US")
    case "France":
        print("Fr")
    case "Germany":
        print("De")
    case _:
        print("Unknown")

#python challenge
##Validate the quality nd correctness of email values

email = "4saint@gmail.org".strip() #cleans up space first
#must not be empty
if email == "":
    print("email must be inputted")
#must contain '.' and '@'
if '.' not in email and '@' not in email:
    print("email must include '.' and '@'")
#must contain exactly one "@"
if email.count('@') > 1:
    print("email must contain excatly one @.")
#must end with ".com" ,".org" or ".net"
if not email.endswith((".com",".org",".net")):
    print("email must include .com,.net or .org")
#must not be longer than 200 characters
if  len(email) > 200:
    print("email must be less than 200 chars")
#must start and end with a letter or digit.
if email.isalnum():
    print("email can't contain special characters")
else:
    print('email is valid')

#Python challenge
#validate the quality and correctness of passwords
password = "saintgmailorg ".strip()
email = "4saint@gmail.org"
#must not be empty
if password == "":
    print("password must not be empty")
#must be atleast 8 characters
if len(password) < 8:
    print("password must not be less than 8 characters")
#must include at least one uppercase
if  len(password.upper()) <= 0 : 
   print("password must contain one uppercase")
#must include atleast one lowercase
if len(password.lower()) == 0: 
   print("password must contain one lowercase")
#must not be same as d email
if password == email: 
   print("password must not be same as email")
#must not contain any spaces
if  " " in password: 
   print("password must not contain spaces")
#must start and end with a letter or digit.
if not password.isalnum(): 
   print("password must start and end with a letter")
else:
    print("password is strong and valid")

