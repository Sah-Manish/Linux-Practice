import sys
x=sys.argv[1]
print("{} ke pahade".format(x))
for i in range(1,11):
    print("{0} * {1} = {2}".format(x,i,int(x)*i))

