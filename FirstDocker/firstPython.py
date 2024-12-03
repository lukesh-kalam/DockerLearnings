list1 = [1,2,3,4,5,6]
output = []
k = 7

for i in range(len(list1)):
    for j in range(len(list1)):
        if j>i :
            if list1[i]+list1[j]==k:
                list2 = [list1[i],list1[j]]
                output.append(list2)

#print(output)
tupl1 = tuple(output)
print(tupl1)
print(tupl1[::])

#for i in range(len(tupl1)):
#    print(tupl1[i])

for i in tupl1:
    print(i)
print(tupl1.count([1,6]))