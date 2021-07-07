import datetime
customer={'accountNo':435674366, 'balance':567788}
currentTime=datetime.datetime.now().hour

def fundTransfer(fromAccountNo,toAccountNo,amount):
    if(customer['accountNo'] == fromAccountNo):
        if(customer['balance']>amount):
            if(currentTime>18):
                print("Fund Transfer will happen in next working day")

            else:
                balance=customer['balance']-amount
                print("Fund Transfer completed", fromAccountNo,toAccountNo,amount,balance)