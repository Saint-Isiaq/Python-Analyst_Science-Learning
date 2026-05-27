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
