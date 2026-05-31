#How to iterate
#Task
ltrs = ['a','b','c']
nw_lst = []
for l in ltrs:
#Or
 nw_lst.append(l.upper())
print(nw_lst)

#Enemerator  #prints values with their index/position
ltrs = ['a','b',' ','c']
print(list(enumerate(ltrs)))  #or
print(list(enumerate(ltrs,start=1))) #0r
for index, value in enumerate(ltrs):
  print(index,value)

#Reversed 
ltrs = ['a','b',' ','c']
#print(list(reversed(ltrs))) #or
for l in reversed(ltrs):
  print(l) 

#Zip #for combination of two variables
ltrs = ['a','b',' ','c']
nos = [1,2,3,4]
#print(list(zip(ltrs,nos))) # 0r
for l,n in zip(ltrs,nos):
  print(l,n)

#Iterator Map  
# #Task:make evry ltrs uppercase
ltrs = ['a','b','d','c']
print(list(map(str.upper,ltrs)))
#case 2 #task: convert list items to integers
nos = [1,2,3,4]
print(list(map(int,nos)))
#case 3 #clean list ,remove all unwanted spaces
nom = [' maria ','kumar ',' alio']
#print(list(map(str.strip,nom))) #or
for n in map(str.strip,nom):
  print(n)

#Filter Iterators #to filter bad datas
#Task: clean up list,remove bad data
ltrs = ['a','b',' ',None,'c',False]
print(list(filter(None,ltrs))) #Or
print(list(filter(bool,ltrs))) #returns same
#task: Keep only letters in items
items = ['sql','123','python','42']
#print(list(filter(str.isalpha,items))) #removes any semblance of an INT
# or
for i in filter(str.isalpha,items):
  print(i)



#LAMBDA Fn(function)
multiply = lambda x: x*3
print(multiply(500))
#case 2
add = lambda x, y : x + y
print(add(13,26))
#case3
multiple = lambda a,b : a * b
print(multiple(25,65))

#LAMBDA + MAP 
#task : prices are stored as messy str and need cleaning to floats
prices = ['$12.50','$11.05','$43.32','$32.54']
#p='$12.50'
#print(float(p.replace('$','')))
print(list(map(lambda p: float(p.replace('$','')),prices)))

#LAMBDA + FILTER
#task: remove all prices lower than 100
prices = [120,45,231,543,99,87]
print(list(filter(lambda p: p >= 100,prices)))
#case 2
#on  #nested list #keep only students with scores higher than 70
eleves = [
  ['mara',84],
  ['kuma',90],
  ['max',60]
]
print(list(filter(lambda e: e[1] >= 70,eleves)))

#Python Challenge
#Keep only Students with Names Starting with 'M'
eleves = [
  ['mara',84],
  ['kuma',90],
  ['max',60]
]
print(list(filter(lambda e: e[0].startswith('m'),eleves)))

#LIST Comprehension
#Task :#Normalize d domains into standard Format
domains = [
  'www.google.com',
  'openai.com',
  'localhost',
  'WWW.DATAWITHBARAA'
]

cleaned = [#Data transformation
          d.lower().replace('www.','')
           #For loop
          for d in domains
          #Data Filtering
          if '.' in d
          ]
print(cleaned)

#Data Structure #TUPLES
Tuple = (10,20,30,20)  #ORDERED like List
print(Tuple)
#Allows Duplicates
print(Tuple[1])  #INDEXED
Tuple[3] = 40  #IMMUTABLE # cant be changed
print(Tuple) 

# DATA STRUCTURE #SETS
my_lst = {10,20,45,20}  #UNORDERED unlike the list
# NO DUPLICATION Allowed
my_lst.remove(20) #MUTABLE :#Can be changed
print(my_lst)
print(my_lst[1])  #Not INDEXED

#METHODS FOR Working SETS
a = {10,20,30,45}
#Adding
a.add(23)

#Update #add groups of value
a.update("hey")
#case 2
a.update({11,15}) #or Shortcut
a |= {2,3}
print(a)

#Removing
a = {10,20,30,45}
a.remove(45)
#case 2 that leads to error
a.remove(15)  #removing value not in #SET #Instead 
#discard
a = {10,20,30,45}
a.discard(15)
print(a)

#MATH METHODS FOR SETS
a = {10,20,30,45}
b = {43,10,25,30}
#UNION
print(a.union(b)) #Or #SHortcuts
print(b|a)

#intersection
print(a.intersection(b)) #or #Shortcuts
print(b&a)

#difference
print(a.difference(b)) #or #Shortcuts
print(b-a)

#symetric_difference
print(a.symmetric_difference(b)) #or #shortcuts
print(b^a)

#RELATIONSHIP Method For SEts
a = {10,20,30,45}
b = {43,10,25,30}
print(a.issubset(b))
#Issuperset
print(b.issuperset(a))
#Isdisjoint
print(a.isdisjoint(b))

#DICTIONARY(Dict)
my_dict = {'a':10,'b':20,'c':30,'d':20} #ORDERED
#Allows DUPLICATES
#Cant be Indexed  but 
print(my_dict['c'])   #KEYS can be called
my_dict['d'] = 35
print(my_dict['d'])  #IS Mutable #can be changed

#DICT METHODS
user = {'id':2,'age':23,'city':'berlin'}
#How to Access Dict
print(user['age']) #or
#case 2 #that leads to error #if not foundn in dict
#print(user['nom'])
#Case 3 #using a safer method
#get()
print(user.get('nom')) #or
#case 3.5
print(user.get('nom','key not found'))

#HOW TO CHECK
user = {'id':2,'age':23,'city':'berlin'}
#In Operator
print('age'in user) #or
print('nom'not in user)

#View OBJECTS inside Dict
user = {'id':2,'age':23,'city':'berlin'}
#KEYS
print(user.keys())
#Values
print(user.values())
#Items
print(user.items())

#Looping Dicts
user = {'id':2,'age':23,'city':'berlin'}
for u in user:
  print(u,user[u]) #instead #Do
#Case 2
for key,value in user.items():
  print(f'\n{key},{value}')

#CHANGING DICT
user = {'id':2,'age':23,'city':'berlin'}
#Adding
user['nom'] = 'mateo'
print(user)
#Case 2
#Changing Value
user['age'] = 24
print(user)
#Updates  #updating multiple values
user.update({'age':30,'city':'paris'})
print(user) 
#Removing from DICT
#POP()
user = {'id':2,'age':23,'city':'berlin'}
user.pop('age')
print(user)  #OR 
#Case 2 That returns an Error
user = {'id':2,'age':23,'city':'berlin'}
user.pop('nom') #So instead we pass a value if key not found
#Case 2.5
nom = user.pop('nom','key not found')
print(user)
print(f'removed item: {nom}')
#POPITEM()  #removes last item added to dict
user = {'id':2,'age':23,'city':'berlin','nom':'mario'}
user.popitem()
print(user)

#CREATION OF NEW DICT
user = {'id':2,'nom':'mario','age':23,'city':'berlin'}
#instead of the usual
#FromKeys()
user = dict.fromkeys(['id','nom','role','city'],None)
print(user)

#DICT challenge
user = {'id':2,'nom':'Johna','age':23,'city':'Berlin'}
#Create new dict
new_dict = {
  #DATA expression/transformation
k.upper(): v.lower()
#for loop
for k, v in user.items()
#data filtering
if isinstance(v,str)
}

print(f'new dict: {new_dict}') 