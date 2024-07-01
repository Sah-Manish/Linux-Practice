#Password manager
import sys
if(len(sys.argv) < 2):
    print("Usage: python password.py [account name]")
    sys.exit()
account=sys.argv[1]
print(account)
