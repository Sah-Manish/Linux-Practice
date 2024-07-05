import sys
s=sys.argv[1:]
arr={}
for i in s:
    for j in i:
        arr.setdefault(j,0)
        arr[j]+=1
print(arr)
