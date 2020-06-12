#lst = []

# number of elemetns as input

# iterating till the range
#for i in range(0, n):
#    ele = int(input("enter weight in lbs: "))

#    lst.append(ele)
# adding the element

n = int(input("Enter number of students : "))
lst=[int(input("enter weight in lbs: ")) for i in range(0, n)]
print(lst)
kg = [pounds * 0.453592 for pounds in lst]
print(kg)