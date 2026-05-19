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
domains = [
  'www.google.com'
  'openai.com'
  'localhost'
  'WWW.DATAWITHBARAA'
]