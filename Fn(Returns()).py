#Function type by purpose
#Action functions   #Validation function  #transformation function #orchestration function()

#Action fn()
#Case 1.0 
#task: store application log messages in a file whenever an event occurs
def log_write(message):
    with open(r"c:\Users\USER\Documents\Python(Analyst_Science) Learning\python\app.log", "a") as file:
        file.write(message + "\n")
#fn(📞)
log_write("app processing")
log_write("app starting")
log_write("User successfully Logged in")
log_write("app stopped")


#transformation Function()
#Case 1.1
#Task:  clean email addresses and split them into structured data
#Username + #Domain
def mail_cleaning_and_split(email):
    """cleaning up the emails input from user"""
    cl_email = email.strip().lower()
    #SaInt0Th@gmail.com
    """splitting mail address into username and domain"""
    username, domain = cl_email.split("@")
    return  {f'username: {username}, domain: {domain}'}
#fn(📞)
print(mail_cleaning_and_split('Saint0Th@gmail.com'))


#Validation Function()
#Case 1.2
#task: Check whether d password meets d minimum required 8 password chars
def is_valid_password(password):
    return len(password) >=  8
#fn(📞)
print(is_valid_password('Saint0th'))

#Case 1.2.1
#Task: Checks if email has the basic format
def is_valid_email(email):
    "@" in email and "." in email
    return email
#fn(📞)
is_valid_email('Saint@gmail.com')

#Orchestration function() #Decides which fn() to call for a job
#Case 1.3
#MINI-PROJECT
log_write('app started')
#receive an email from the user
email = input("please enter a valid mail address")
#validate the email
if not is_valid_email(email):
    log_write(f'invalid email entered: {email}')
#if it is valid, clean and structure the email
else:
    cl_mail = mail_cleaning_and_split(email)
    log_write(f'email processed: {cl_mail}')
#log each step of the program
log_write('app stopped')