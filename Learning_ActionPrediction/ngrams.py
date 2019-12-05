"""
    Gagan Heer A00933997
    Learning: Action Prediction Ngrams
    Please look over the README.md file if there is any trouble using this file
"""
import random
import re

patterns = dict()

def ngrams():
    print("R = Rock, P = Paper, S = Scissors\n")
    data = ''
    quit = False
    gameNum = 1
    bigram = None
    playerScore = 0
    botScore = 0
    mostOccurences = 0
    mostLikelyMove = None
    # Keep playing as long as the player doesn't quit
    while quit == False:
        playerAction = (input('Select an option (R,P,S) or Q to Quit: ')).upper()
        if playerAction in 'RPS':
            
            # If there is enough data then make a bigram and update the dictionary
            print('Game Num: ', gameNum)
            data += playerAction
            if(len(data) >= 3):
                bigram = data[len(data)-3:-1]
                newMove = data[len(data)-1]
                if bigram + newMove in patterns:
                    patterns[bigram + newMove] += 1
                else:
                    patterns[bigram + newMove] = 1
                print('Bigram: ', bigram)
                print('Players Last Move: ', newMove)

            # If not enough data collected yet (less than 3 games played) then choose a random action
            if(bigram == None):
                botAction = get_action(None)
                
            # If there is enough data to create a bigram then try to beat the most likely choice
            else:
                # Find all keys that match the bigram that was created from the previous players move
                bigramMatches = []
                for key in patterns:
                    if bigram in key[0:2]:
                        bigramMatches.append(key)

                # Iterate over all the bigram matches to find the move that is most likely to occur next
                for match in bigramMatches:
                    if patterns[match] > mostOccurences:
                        mostOccurences = patterns[match]
                        mostLikelyMove = match[-1]
                if(mostOccurences > 0):
                    print('Players Most Likely Move: ', mostLikelyMove)
                mostOccurences = 0
                botAction = get_action(mostLikelyMove)
                # Uncomment for random Rock, Paper, Scissors decisions
                #botAction = get_action(None)

            print('You Selected: ', playerAction)
            print('Bot Selected: ', botAction)
            result = get_result(playerAction, botAction)
            print(result)
            if(result == 'You Win'):
                playerScore += 1
            elif(result == 'You Lose'):
                botScore += 1
            print('Your Score: ', playerScore)
            print('Bot Score: ', botScore)
            gameNum += 1
        elif playerAction in 'Q':
            quit = True
            print('---Final Score---\nYou: ', playerScore, '\nBot: ', botScore, '\nThanks For Playing')
        else:
            print('Please select a valid option')
        print("\n\n")

def get_result(playerAction, botAction):
    result = None
    if playerAction == botAction:
            result = 'You Tie'
    elif playerAction == 'R':
        if botAction == 'P':
            result = 'You Lose'
        else:
            result = 'You Win'
    elif playerAction == 'P':
        if botAction == 'S':
            result = 'You Lose'
        else:
            result = 'You Win'
    else:
        if botAction == 'R':
            result = 'You Lose'
        else:
            result = 'You Win'

    return result

def get_action(playerMostLikelyMove):
    # Return best action
    if playerMostLikelyMove == 'R':
        return 'P'
    elif playerMostLikelyMove == 'P':
        return 'S'
    elif playerMostLikelyMove == 'S':
        return 'R'
    else:
        # Return random action if no likely move is identified
        botAction = random.randrange(0,3)
        if botAction == 0:
            return 'R'
        elif botAction == 1:
            return 'P'
        elif botAction == 2:
            return 'S'

if __name__ == '__main__':
    ngrams()
