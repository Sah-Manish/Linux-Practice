import sys
s=" ".join(sys.argv[1:])
arr={}
for i in s:
    arr.setdefault(i,0)
    arr[i]+=1
print(arr)
