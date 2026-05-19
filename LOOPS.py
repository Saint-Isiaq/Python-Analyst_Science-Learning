#Loop Statements  #For Loops et #While Loop
#For LOOP
for files in (1,2,3,4,5):
    print("file round:", files)  #basic use case
    
#case 2 #using round
files = ('sama','sinca','soma','sona')
for file in files:
    print(f' est ton nom. Pas vrai? :{file}')

#Range in Loop
for files in range(1,6):
    print(f'file round: {files}') #range stop,start.
#case 2 #range step
for files in range(1,15,2):
    print(f'file round: {files}') #range stop,start, et step
#case 3
scores = [23,43,65,87,98]
total = 0
for score in scores:
    total += score
    print('current total:', total)
print('final total:', total)

#Case 4  #cleaning data
files = [' report.csv','data.csv ',' ',' final.txt ']
for file in files:
     file = file.strip().replace('.txt','.csv')
     print(f'processing: {file}')

#1 Python challenge
#print the 7 times table from 1 -10 using a For Loop.
rag = [1,2,3,4,5,6,7,8,9,10]
Range = 7
n = 0
for r in rag:
    r *= Range
    n += 1
    print(f'{Range} * {n} = {r}')  #Mannnn! Got it but took so long, lol

#2 python challenge
#print a left aligned pyramid of stars with 6 rows using a FOR LOOP. 
xar = ['*','*','*','*','*','*']
c = str(0).replace(str(0),'')
for x in xar:
    c += str(0).replace(str(0),'*')
    print(f'{c}')  #phew!, finally got it after an hour trial.

#LOOPS CTRL Statement   #Break-Statement 
names = ['john','mata','','Kuma']
for name in names:
    if name ==  (''):
        print('Empty value detected')
        break  #Stops the code when bad data is detected
#case 2 #To continue the Break
names = ['john','mata','','Kuma']
for name in names:
    if name ==  (''):
      print('Empty value detected')
      break
    print(f'name = {name}') 

#Continue Statements
names = ['john','mata','','Kuma']
for name in names:
    if name ==  (''):
        print('Empty value detected')
        continue
    print(f'name = {name}')  
#Pass Statements 
names = ['john','mata','','Kuma']
for name in names:
    if name ==  (''):
        pass ##To-do: we coming here later
    print(f'name = {name}')

   #Real-World applications of #Break and #Continue
#Task 1
days = ['mon','wed','sat','fri','sun']
for day in days:
    if day in ['sat','sun']:
        continue
    print(f'working days: {day}')
#case 2
days = ['mon','wed','sat','fri','sun']
weekends = ['sat','sun']
for day in days:
    if day in weekends:
        continue
    print(f'working days: {day}')

#Task 2
emails = [
    'siant@gmail.com',
    'saint@outlook.de',
    'DROPTABLE USERS;',
    'Maria@gmail.com'
          ]
for mail in emails:
    if ';' in mail:
       print('SQL injection: hacker Attack')
       break
    print(f'processing email: {mail}')

#Else Statements #Use only with Loops If there's a Break
#Task
items = [1,3,4,7,9,10]
for i in items:
    if i % 2 == 0:
        print('even number found')
        break
else:
    print("all numbers are odd")

# #Else use case #to search and validate data
#Task:check for missing value 
names = ['john','mata',None,'Kuma']
for name in names:
    if name ==  None :
     print('Found a missing name')
     break
else:
 print('All names are accounted for')

#Task #Validation use case for Else
files = ['data0.csv','data1.pdf','data2.csv','data3.txt']
for file in files:
  if not file.endswith('.csv'):
    print(f'{file} is not a csv')
    break
else:
    print(f'All {file} are csv')

#python challenge
file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in file_list:
    if file != 1:
        print(f'{file} has a duplicate')
        break
else:
    print('All files are genuine')

#Nested For Loop
for x in (1,2,3):
    for y in (1,2):
        print(f'{x}{y}')
#Use Cases  #Crossing with Nested Loops
colors = ['green','blue','brown']
sizes = ['L','M','S']
for color in colors:
    for size in sizes:
        print(f'{size}:[{color}]')
#Hierarchy drilling With Nested Loops
years = [2025,2026]
months = ['jan','feb']
day = range(1,30)
for year in years:
    for month in months:
        for d in day:
            print(f'report of: _{year}_{month}_{d}.csv')

#Real_Use_Case Task
#Select Count(*) From customers where id is null
tables = ['customer','Orders','Products','Prices']
columns = ['id','create_date']
for t in tables:
 for c in columns:
     print(f'SELECT COUNT(*) FROM {t} WHERE {c} IS NULL')

#While LOOPS 
i = 1
while i < 6:
  print(i)
  i += 1
  
#Task Write a program that keeps asking question unless True
answer = " "
while answer != "yes":
    answer = input('You are very dull: (Yes/No):')
print('i just knew it')  #lol

#While TRue LOOP
while True :
    answer = input('You are very dull: (Yes/No):')
    if answer == "Yes" :
     break
print('i just knew it') 

#Python Challenge 
attempt = 0
while answer < 3:
    answer = input(f'You are very dull: (Yes/No):')
    if answer == "Yes" :
     print(f'Glad we are on the same Page')
     break
    attempt += 1
else:
 print(f'3 strikes, you are out') #Got it

