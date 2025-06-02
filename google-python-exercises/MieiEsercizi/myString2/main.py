import myString2

def main():
    
    #Esercizio 1: verbing
    #print(myString2.verbing('sightsee'))
    
    #Esercizio 2: not_bad
    message = 'This movie is really not what I have always thought, according to universal laws, would be bad!'
    #print(myString2.not_bad(message))
    
    token1 = 'not'
    token2  = 'bad'
    newToken = 'good'
    print(myString2.replaceBetweenTokens(message,token1, token2, newToken))
    
    
#LAUNCH MAIN SCRIPT    
if __name__ == '__main__':
    main()