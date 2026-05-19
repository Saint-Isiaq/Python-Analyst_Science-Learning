#Data Structures
#Creating Lists
empty_list = []  #3mpty list
mixed_list = [1,2,'b','c',True] #mixed list
nos = [1,2,4,6,9]
#or  #to call list function
tex = 'python'
print(list('python'))

# Nested LIsts #list in a list
matrix = [['a','d','c',1],
   ['e','f','g',2]]

#Accessing and Reading LIst #Indexing
mixed_list = [1,2,'b','c',True] #mixed list
nos = [1,2,4,6,9]
#Task #first item in the list
#last item in the list
print(mixed_list[-1])

#Task
#get the whole list
#Get g in the matrix List
#get the whole row from second row in the matrix
matrix = [['a','d','c',1],
   ['e','f','g',2]]
print(matrix[1])

#Slicing
#Task
#first 2 rows list from list and last 2 rows
#last  items from d last row
matrix = [['a','d','c',1],
   ['e','f','g',2],
   ['i','j','k',3]]
print(matrix[2][2:])

#Unpacking a List
person = ['mara',22,'Data analyst','spain']
#unpacking
name,age,role,country = person

#Unpacking a List #Rest Collector *
person = ['mara',22,'Data analyst','spain']
name,*special = person
print(*special)

#Skipping Items In a List (_)
person = ['mara',22,'Data analyst','spain']
name, _ ,role, _ = person
print(_)  #hmm, we'll see

#How to explore and Analyse Data Structures
numbers = [1,2,3,6,8,6]
print("max;", max(numbers))  #Max
print("min;", min(numbers))  #Mix
print("sum;", sum(numbers))  #Sum
print("length;",len(numbers)) #length
#or
print("All;", all(numbers)) #All
print("Any;", any(numbers)) #Any
#or
print("count;", numbers.count(6)) #count
print("Index;", numbers.index(3)) #index
#or
print(3 in numbers)  #In  operator
print(4 in numbers)
print(3 not in numbers)
#or
list1 = [1,2,5]
list2 = [1,2,4]
print(list1 == list2) #== operator
print(list1 > list2)  #> operator

#How to change list
#Adding new items  #append() #index() #Insert()
mtx = ['a','d','c',1]
  # ['e','f','g',2],
  # ['i','j','k',3]]
#append()
mtx.append('x')
mtx.append('y')
#########
mtx = ['a','d','c']
#index
mtx.index(1, 'y')
print(mtx)
#Insert   
mtx = [['a','d','c',1],
   ['e','f','g',2],
   ['i','j','k',3]]
mtx.insert(0,['a','b','b'])
mtx[2].append('x')
mtx[0].append('y')
print(mtx)

#Removing Variables #clear() #pop()
ltrs = ['a','d','c']
#ltrs.pop()  #removes last items automatically
#ltrs.clear()  #clears all data
trash = ltrs.pop(1)
print(ltrs)
print('removed ltrs;',trash )

#Removing from the matrix
mtx = [['a','d','c',1],
   ['e','f','g',2],
   ['i','j','k',3]]
mtx[0].pop(2)
mtx[1].pop(-1)
mtx[-1].pop(-1)
print(mtx)

#How to Update
#Overwriting
ltrs = ['a','b','d','c']
#ltrs[3]='e'
ltrs[0] = 'x'
ltrs[1]= 'y'
print(ltrs)
#updating for nested list
mtx = [['a','d','c',1],
   ['e','f','g',2],
   ['i','j','k',3]]
mtx[-1] = ['x','y','z',3]
mtx[0][0] = 'x'
mtx[1][0] = 'y'
mtx[-1][-1] = 4
print(mtx)

#How to Order
#(Sort)  #Ascending Order
ltrs = ['c','b','a','d',]
ltrs.sort()
#Reverse true #Descending order
ltrs = ['a','b','d','c']
ltrs.sort(reverse=True)
print(ltrs)
#Ordering for Nested list
mtx = [['a','d','c'],
       ['e','f','g'],
       ['k','j','i']]
mtx.sort()
mtx[-1].sort()
print(mtx)

#Sorting without changing the list
ltrs = ['a','b','d','c']
nw_lst = sorted(ltrs,reverse=True)
print(f'original list: {ltrs}')
print(f'sorted lst: {nw_lst}')
#Reversing
ltrs = ['a','b','d','c']
nw_lst = list(reversed(ltrs))
#ltrs.reverse()
print(f'original list: {ltrs}')
print(f'sorted lst: {nw_lst}')

#How to Copy  #Assignment:Affects both list when one changes
ltrs = ['a','b','d','c']
ltrs_copy = ltrs
ltrs.append('g')
print(f'{ltrs} \n{ltrs_copy}')

##Shallow copy #.copy() #changes are independent of main value
ltrs = ['a','b','d','c']
ltrs_copy = ltrs.copy()
ltrs_copy.append('p')
print(f'{ltrs} \n{ltrs_copy}')
##for nested list
mtx = [['a','d','c'],
       ['e','f','g'],
       ['k','j','i']]
mtx_copy = mtx.copy()
mtx_copy[-1].append('p')
print(f'{mtx} \n{mtx_copy}')
#case2
a = [1,[]]
b = a.copy()
b[1].append(2)
print(f'{a},{b}')  #challenge on ytube

##Deepcopy  #creates a genuine independent copy even in nested list
#import 
import copy
mtx = [['a','d','c'],
       ['e','f','g'],
       ['k','j','i']]
mtx_copy = copy.deepcopy(mtx)
mtx_copy[-1].append('p')
print(f'{mtx} \n{mtx_copy}')

#How To Combine   #(+) operator
ltrs = ['a','b','d','c']
nos = [1,3,4,6]
comb = ltrs + nos
print(comb)
#Extend()  #it extends existing list not create new ones
ltrs = ['a','b','d','c']
nos = [1,3,4,6]
nos.extend(ltrs)
print(f'{ltrs} \n{nos}')
#Zip() fn()  #Creates a tuple list when combining
ltrs = ['a','b','d','c']
nos = [1,3,4,6]
comb = list(zip(ltrs,nos))
print(f'{comb}') 

#Task:
ids = [102,103,105]
nom = ['mario','alin','orio']
print(list(zip(nom,ids)))
