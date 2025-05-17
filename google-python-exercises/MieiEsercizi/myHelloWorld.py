import myHelloWorldUtils
import random


'''
Ciao, Mario, brutta testa di cazzo!
'''

def main():
    
    name = myHelloWorldUtils.getName()
    message = myHelloWorldUtils.buildMessageWithName(name)
    message = myHelloWorldUtils.multiplyMessage(message, random.randint(1, 10))
    
    print('-'*20)
    print(message)
        


if __name__ == '__main__':
    main()
# This is the standard boilerplate that calls the main() function.