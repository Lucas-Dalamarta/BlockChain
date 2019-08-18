###############################################################################
global BlockChain , Choice
###############################################################################
Choice  =   1
owner   = 'Luk3'
BlockChain  =   [[1]]
genesysBlock    =   {
    'PreviousHash':'',
    'Index':0,
    'Transactions':[]
}
openTransactions    =   []
###############################################################################
def messages(code):
    """ Receives a code , acording to which message is to be shown \n
        1 : ValueError
    """
    #   I thought about passing the errors as arguments, but dropped it
    #   Might come back later
    
    if      code == 1:  return  print("Invalid value , please , Try Again")
    elif    code == 2:  return  print("")


def printChar(char):
    return  print(char*60)


def mineBlock():
    """ Mines a new block , for now , it uses standard values"""
    lastBlock = BlockChain[-1]
    block = {   
            'PreviousHash':'ABC',
            'Index':len(BlockChain),
            'Transactions':openTransactions
            }
    BlockChain.append(block)
    pass


def lastValue():
    """Returns BlockChain last value"""
    return  BlockChain[-1]


def addTransaction(sender,recipient,amount=1.0):
    """ Receives and appends a new value to the BlockChain
        :sender:    Sends the coins
        :recipient: Receives the coins
        :amount:How much coins where transfered in a transacion (Default = 1.0) 
    """

    transaction =   {
        'Sender'    :sender,
        'Recipient' :recipient,
        'Amount'    :amount
    }
    openTransactions.append(transaction)


def getBlockChain():
    """Returns BlockChain"""
    return print(BlockChain)


def getTransactionValue():
    """ Asks for recipent , then how much will be transfered"""
    while True: 
        try:
            amount      =   float(input('Enter the transaction amount:'))
            if amount <= 0:
                raise ValueError
        except  ValueError:
            messages(1)
            continue
        break

    recipient   =   input('Enter recipient of the transaction:')
    
    return(recipient,amount)


def verifyBlockChain():
    for block_index in range(len(BlockChain)):
        if  block_index == 0:
            continue
        elif    BlockChain[block_index][0]  ==  BlockChain[block_index - 1]:
            return True
        else:
            return False

###############################################################################
###                                 MAIN                                    ###
###############################################################################

printChar("*")
print("\tHello ! Welcome to Luk3's BlockChain")
printChar("*")

while Choice != 0:
    print("1 - New transaction :")
    print("2 - Visualize BlockChain :")
    print("3 - Validate BlockChain :")
    print("0 - Quit :")
    print("\n\n\t")
    Choice = int(input())

    if Choice == 1 :
        data_transacition = getTransactionValue()
        addTransaction(data_transacition)
        #addTransaction(getTransactionValue())  ??  Would this work ?
    elif Choice == 2 :
        getBlockChain()
    elif Choice == 3 :
        if verifyBlockChain() == True:
            print("\tCurrent BlockChain is valid !")
        else:
            print("\tCurrent BlockChain is NOT valid !")
    else:
        break
    continue

printChar("*")
print("\tThanks for using Luk3's BlockChain")
printChar("*")

###############################################################################