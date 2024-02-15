

def deposit():
    print("Amount  #### credited into the account......")

def getBalance():
    print("The current balance in the account is ######")


def BankFun(fnc):       # HOF
    print("Logging into the server.....")
    fnc()           # call back
    print("Logging out of the server......")
    print("-" * 60)


BankFun(deposit)
BankFun(getBalance)

