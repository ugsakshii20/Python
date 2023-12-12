from xml.dom.minidom import Element


myList=[10,40,50,20,30,10,40,10]
yourList=['saw','small','foxes','he','six']

#1)Append integer 60 into myList
myList.append(60)
print("List after appending 60:",myList)
#2)Insert 70 on 2nd Position
myList.insert(1, 70)
print("List after inserting 70 at 2nd Position:",myList)
#3)Sort myList in ascending and descending order
myList.sort()
print("List in ascending order:",myList)
myList.sort(reverse=True)
print("List in descending order:",myList)
#4)Sort yourList in ascending and descending to length of strings.
yourList.sort(key=len)
print("List in ascending to lenth of strings",yourList)
yourList.sort(key=len, reverse=True)
print("List in descending order according to length of strings",yourList)
#5)Add float value 3.5 into yourList.
yourList.append(3.5)
print("List after adding 3.5:",yourList)
#6)Use POP and remove method to remove 3.5
yourList.pop()
#yourList.remove(3.5)
print("List after removing 3.5 from list:",yourList)
#7)Create ourList by merging myList and yourList
ourList=myList+yourList
print("List after merging two lists:", ourList)
#8)Find sum of elements in mylist
sum_list=sum(myList)
print("sum of elements from myList:",sum_list)
#9)Find samllest, largest and second largest number in a myList
min_list=min(myList)
max_list=max(myList)
print("Smallest number from list:",min_list)
print("Largest number from list:",max_list)
myList.sort(reverse=True)
print("Second largest number from list is:",max_list)
#10)Count occurences of all element in a list
c={Element:myList.count(element) for element in set(myList)}
print("Counted occurences of elements in list are:",myList)
#11)Perform Data slicing to display string elements from ascending sorted yourList as:
 #a. Display-'saw','six','small'
a=yourList[:3]
print("sorted list a",a)
 #b. Use negative indices to display - 'six','small','foxes'
b=yourList[-3:]
print("sorted list b:",b)
 #c. All elements after mid of the list(In both directions)
middle=len(yourList)//2
print("Middle of the list is:",middle)
m1=yourList[::2]
print(m1)
m2=yourList[-1::-2]
print(m2)
