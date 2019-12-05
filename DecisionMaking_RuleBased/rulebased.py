"""
    Gagan Heer A00933997
    Decision Making: Rule Based
    Please look over the README.md file if there is any trouble using this file
"""
import time
import gym
import blackjack as bj
import random

env = bj.BlackjackEnv()
STAND = 0
HIT = 1
numGames = 1001

# 1 = hit, 0 = stand
def rule_based_action(playerTotal, dealerCard):
    nextAction = None
    if playerTotal <= 11:
        nextAction = HIT
    elif playerTotal >= 17:
        nextAction = STAND
    elif dealerCard >= 7 or dealerCard == 1:
        nextAction = HIT
    elif (dealerCard <= 6 and dealerCard != 1) and playerTotal >= 13:
        nextAction = STAND
    elif dealerCard == 2 or dealerCard == 3:
        nextAction = HIT
    else:
        nextAction = STAND
    return nextAction    

def play_game():
    numWins = 0
    numLoss = 0
    numDraw = 0
    result = None

    for i in range(numGames):
        done = False
        totalReward = 0
        round = 0
        state = env.reset()

        print('\n\n\nSTARTING HAND')
        print ('Player Cards:', state[3])
        print('Player Total:', state[0])
        print('Dealer Show Card:', state[1], '\n')
        nextAction = rule_based_action(state[0], state[1])
        # Uncomment for random actions
        #nextAction = random.randrange(2)
        while not done:
            round += 1
            observation,reward,done,info = env.step(nextAction)

            print('Round ', round)
            print('Action ', 'Stick' if nextAction == 0 else 'Hit')            
            print ("Player Cards:", observation[3])
            print("Player Total:", observation[0])
            if(done):
                print ('Dealer Cards:', observation[4])
                dealerTotal = sum(observation[4])
                # Make sure aces display as adding 11 to the dealer's total when required
                if(dealerTotal <= 16 and observation[0] <= 21):
                    dealerTotal += 10
                print('Dealer Total:', dealerTotal)
            else:
                print('Dealer Show Card:', observation[1])
            print('Done Drawing: ', done, '\n')

            nextAction = rule_based_action(observation[0], observation[1])
            # Uncomment for random action
            #nextAction = random.randrange(2)
            totalReward += reward

        if totalReward >= 1:
            result = 'You Win'
            numWins += 1
        elif totalReward <= -1:
            result = 'You Lose'
            numLoss += 1
        else:
            result = 'Draw'
            numDraw += 1

        print('------------------------------------')
        print('Game Number', i,' Result: ', result)

    print('\n\nFINAL RESULTS')
    print('=================================')
    print('Total Wins: ', numWins)
    print('Total Losses: ', numLoss)
    print('Total Draws: ', numDraw)

if __name__ == '__main__':
    play_game()
