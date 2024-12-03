#Prime Number Check Number:wq!

num = 44
count =0
for i in range(2,int(num/2)+1):
    if num%2 ==0:
        count += 1
if count==0 :
    print("Prime Number ")
else :
    print("Not Prime")
