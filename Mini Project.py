#MINI-PROJECT
#receive an email from the user
#validate the email
#if it is valid, clean and structure the email
#log each step of the program

def log_write(message):
    """#Action fn():
        This logs what part of the step has any issue
    or what part is succesful.
    App.log(): Where the logs message get sent to. """
    with open(r"c:\Users\USER\Documents\Python(Analyst_Science) Learning\python\app.log","a") as file:
         file.write(message + "\n")

def mail_cleaning_and_split(email):
   """#Transformation fn():
        This helps in cleaning raw data into usable ones
    We have made this one to clean
       and also split user email input and their domain apart"""
   cl_mail = email.strip().lower()
   username , domain = cl_mail.split("@")
   return {f'username: {username}, domain: {domain}'}

def is_valid_email(email):
   """#Validation fn():
      This heps us in validating raw data from user email input.
      We invalidate email if "@" isn't in password 
      or "."   """
   if "@" in email and "." in email:
    return f'{email} valid'  
   
   

#We Have received an email from a User
def process_user_email(email):
 """Orchestration fn():
    This combines multiple fn(), and decides which to call for a role
    Combines: #Action fn(), #Validation fn() and #Transformation fn() in one fn()"""
 log_write("app started")
#checking if it is valid
 if not is_valid_email(email): 
  log_write(f"invalid email entered: {email}")
#if valid we clean and store structured information
 else:
   cl_mail = mail_cleaning_and_split(email)
   log_write(f'email processed succesfully: {cl_mail}')

#Trying to get user email input
email = input("please enter a valid email:")
#fn(📞)
process_user_email(email)
log_write('app stopped \n')