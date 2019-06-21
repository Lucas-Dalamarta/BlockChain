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


formats("-",60)
print("\tHello ! Welcome to Luk3's BlockChain")
formats("-",60)

while Choice != 0:

    print("1 - For new entry :")
    print("2 - To visualize BlockChain :")
    print("0 - To quit :")
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
    else:
        break
    continue

formats("*",60)
print("\tThanks for using Luk3's BlockChain")
formats("*",60)