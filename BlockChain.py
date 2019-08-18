###############################################################################
global BlockChain , Choice
###############################################################################
Choice  =   1
owner   = 'Luk3'
genesisBlock    =   {
    'PreviousHash':'',
    'Index':0,
    'Transactions':[]
}
BlockChain  =   [genesisBlock]
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
    
    #   With List Comprehensions
    hashedBlock =   ' - '.join([str(lastBlock[key]) for key in lastBlock])
    #   SO , the .join function , goes through the List , and appends a  ' - ' between elements , but it only works in strings , which is why str was used

    #   Without List Comprehensions    
    #   hashedBlock would have to be turnt = '' then a for loop to get the values required for the hash
    #   for key in lastBlock:
    #       value = lastBlock[key]
    #       hashedBlock = hashedBlock + str(value)
    
    block = {   
            'PreviousHash':hashedBlock,
            'Index':len(BlockChain),
            'Transactions':openTransactions
            }
    BlockChain.append(block)


def lastValue():
    """Returns BlockChain last value"""
    return  BlockChain[-1]


def addTransaction(recipient,amount=1.0,sender=owner):
    """ Receives and appends a new value to the BlockChain \n
        Recipient: Receives the coins  \n
        Amount: How much coins where transfered in a transacion (Default = 1.0) \n
        Sender: Who is sending the coins (Default = owner)\n
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
    recipient   =   input('Enter recipient of the transaction:')

    while True: 
        try:
            amount      =   float(input('Enter the transaction amount:'))
            if amount <= 0:
                raise ValueError
        except  ValueError:
            messages(1)
            continue
        break
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
    print("4 - Mine Block :")
    print("0 - Quit :")
    print("\n\n\t")
    Choice = int(input())

    if Choice == 1 :
        data_transaction = getTransactionValue()
        sender , amount = data_transaction
        addTransaction(sender , amount)
        
    elif Choice == 2 :
        getBlockChain()
    elif Choice == 3 :
        if verifyBlockChain() == True:
            print("\tCurrent BlockChain is valid !")
        else:
            print("\tCurrent BlockChain is NOT valid !")
    elif Choice == 4:
        mineBlock()
    else:
        break
    continue

printChar("*")
print("\tThanks for using Luk3's BlockChain")
printChar("*")

###############################################################################