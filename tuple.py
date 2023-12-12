myTuple=(10,20,30)
yourTuple=("Pune","Mumbai","Delhi")
mixTuple=('Foo',[1,2,3],'True')
nestedTuple=(('Wes McKineey','Python for Data Analysis','OReillyMedia'),('Mark Lutz','Programming Python','OReillyMedia'),('Charles Severance','Python for Evverybody','Blumenberg'))
#1) Merge myTuple and yourTuple into ourTuple
ourTuple=myTuple+yourTuple
print("OurTuple=",ourTuple)
#2) Convert myTuple into list myList and reverse
myList=list(myTuple)
myList.reverse()
print("Reversed list is:",myList)
#3) Unpack yourTuple values into three variables - District, State, and National
District, State, National = myTuple
print("District=",District)
print("State=",State)
print("National=",National)
#4) Display all eleemnts of mixTuple
print(mixTuple)
#5) Add 4 into list element of mixTuple
mixTuple[1].append(4)
print("mixTuple with 4=",mixTuple)
#6) Perform algebric operations addition and multiplication on myTuple and yourTuple
sumTuple=myTuple + yourTuple
MulTuple=myTuple*2
print("sum-",sumTuple)
print("mul-",MulTuple)
#7) Access information from nestedTuple and display the information as:
for author, book, publisher in nestedTuple :
    print("Name of Author:",author)
    print("Name of Book:",book)
    print("Name of Publisher:",publisher)
    print("-"*20)
