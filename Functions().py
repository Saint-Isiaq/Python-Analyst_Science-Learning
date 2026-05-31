#Function()
#User Defined Function #Basics
print('start')
def greet():
  print(f"hello, Welcome")
#fn(📞)
greet()
print('end')

#Case 1.0 
def mult_two(x):
  print(x * 3)
#fn(📞)
mult_two(6)

#UDF #Intermediate
#case 1.1
#buillding up a fn()
name = ' MariA '
print(name.strip().lower())
#hardcoded fn() build_up
def clean_code():
  name = ' MariA '
  print(name.strip().lower())
#fn(📞)
clean_code()
#Dynamic fn() Build_up
def clean_code(name):
  print(name.strip().lower())
#fn(📞)
clean_code(' MariA ')
clean_code('SMITH ')

#Global Variables
f = 4  #Global vrble
def multi_tw(x):
 print(x * f)
#fn(📞)
multi_tw(7)

#Local variable
f = 4  #Global vrble #F
def multi_tw(x): #parameter #X
 y = x * f  #lcal vrble #Y
 print(y)
#fn(📞)
multi_tw(10)

#case 1.0.1 #Local variable
def clean_txt(name):
  cleaned = name.strip().lower().replace(" ","") #lcl vrbl
  print(cleaned)
#fn(📞)
clean_txt(' MaRiA ')
clean_txt(' SMAT HY')
clean_txt(' Fo w A VE s')

#case 1.0.2 #global variable
case_rule = " "  #glbl vrble
def clean_txt(name): #parameter
  cleaned = name.strip().lower() #lcl vrbl
  if case_rule == " ":
    cleaned = cleaned.replace(" ","")
    print(f'raw: {name}')
    print(f'cleaned: {cleaned}\n')
#Fn(📞)
clean_txt(' MaRiA ')
clean_txt(' SMAT HY')
clean_txt(' Fo w A VE s')

#UDF #Advanced
#Building Full Clean Name
#Positional Arguments
def clean_name(nom,prenom,country):
  first = nom.strip().lower().replace(" ","")
  last = prenom.strip().lower().replace(" ","")
  name = first + " " + last
  print(f'{name} from {country}')
#Fn(📞)
clean_name(' MaRiA ',' SMAT HY',"DE")
clean_name('EG',' MaRiA ',' Fo w A VE s') #Positional error wont be corrected
clean_name('SMiTHy ',' Fo w A VE s','FR')

#Keyword Arguments
def clean_name(nom,prenom,country):
  first = nom.strip().lower().replace(" ","")
  last = prenom.strip().lower().replace(" ","")
  name = first + " " + last
  print(f'{name} from {country}')
#Fn(📞)
clean_name(country = 'DE', nom = ' MaRiA ', prenom = ' SMAT HY')
#keyword Arguments corrects position error
clean_name(prenom =' Fo w A VE s',country = 'FR' ,nom = 'SMiTHy ')
#if arrangementsbgets messed up, it still works correct

#Mixed Arguments  #Rule:Always starts with #Pos Args
def clean_name(nom,prenom,country):
  first = nom.strip().lower().replace(" ","")
  last = prenom.strip().lower().replace(" ","")
  name = first + " " + last
  print(f'{name} from {country}')
#Fn(📞)
clean_name(' MaRiA ',' SMAT HY',country = 'DE')
clean_name('SMiTHy ',prenom = ' Fo w A VE s',country = 'FR')
#Stick to one of both, forget #Mixed Args

#Default Parameters 
#Rules #parameters with a default fllws one without a default
def clean_name(nom,prenom,country = 'unknown'):
  first = nom.strip().lower().replace(" ","")
  last = prenom.strip().lower().replace(" ","")
  name = first + " " + last
  print(f'{name} from {country}')
#Fn(📞)
clean_name(' MaRiA ',' SMAT HY')  #omitting country argument here
clean_name(' MaRiA ',' Fo w A VE s', 'EG')

#  *ARGS and **KWARGS
#task  #calculating the total of values
def total (a=0,b=0,c=0,d=0):
  print(a+b+c+d) #adding more from three paramtrs

total(2,3,1,4)  #totally stressful instead

#*ARGS
def total(*args):
  print(sum(args))
#fn(📞)
total(2,3,4,5,6,7,8)  #Now adding more arguments without stressing

#Case 2  #**KWARGS
#A mix of different value type 
def user_profile(**kwargs):
  print(kwargs)
#fn(📞)
user_profile( nom = 'christiano',
             prenom ='ronaldo',
             age = 40,
             height = '185cm',
             pays ='portugal')
print(f'\n')
user_profile( nom = 'ademola',
             prenom ='lookman',
             age = 25,
             height = '181cm',
             pays ='nigeria',
             club = 'Ac Milan')