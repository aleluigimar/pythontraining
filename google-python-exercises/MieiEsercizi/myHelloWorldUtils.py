def getName():
    name = input('Qual è il tuo nome? ')
    if name == None or name == '':
        name = 'Mario'
    return name

def multiplyMessage(message: str, n: int) -> str:
    return message * n
            
def buildMessageWithName(name: str) -> str:
    message = 'Ciao, {}, brutta testa di cazzo!\n'.format(name)
    return message