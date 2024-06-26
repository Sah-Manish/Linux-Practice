
#password manager
import sys, pyperclip
pd={"extra7":"laplace", "Sah-Manish":"0003", "admin":"password"}
if(len(sys.argv)<2):
    print("Usage python password.py [account name]")
    sys.exit()
acc=sys.argv[1]
if(acc in pd.keys()):
    pyperclip.copy(pd[acc])
    print("password copied")
else:
    print("no account")
