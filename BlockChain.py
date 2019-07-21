global BlockChain , Choice

#   Initalizing variables
#   Thinking on a way to use OOP in this project , just to be fun
BlockChain  =   [[1]]
Choice      =   1

def messages(sample):
    return  print("Invalid value , please , Try Again")


def formats(text,counts):
    """Returns a print , given character and lenght"""
    printable = ""

    for i in range(counts):
        printable   += text
    return  print(printable)


def lastValue():
    """Returns BlockChain last value"""
    return  BlockChain[-1]


def SetValue(new_value):
    """Receives and appends a new value to the BlockChain"""
    BlockChain.append([lastValue(),new_value])
    return


def getBlockChain():
    """Returns BlockChain"""
    return print(BlockChain)


def verifyBlockChain():
    for block_index in range(len(BlockChain)):
        if  block_index == 0:
            continue
        elif    BlockChain[block_index][0]  ==  BlockChain[block_index - 1]:
            return True
        else:
            return False


formats("-",60)
print("\tHello ! Welcome to Luk3's BlockChain")
formats("-",60)

while Choice != 0:

    print("1 - New transaction :")
    print("2 - Visualize BlockChain :")
    print("3 - Validate BlockChain :")
    print("0 - Quit :")
    print("\n\n\t")
    Choice = int(input())

    if Choice == 1 :
        while True: 
            try:
                value = float(input("Enter value :\t"))
                if value <= 0:
                    raise ValueError
            except  ValueError:
                messages("Error")
                continue
            break
        SetValue(value)
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

formats("*",60)
print("\tThanks for using Luk3's BlockChain")
formats("*",60)