"""
    Gagan Heer A00933997
    Learning: Articial Neural Network
    Please look over the README.md file if there is any trouble using this file
"""
import gym
import random
import numpy as np
import keras
import time
from keras.models import Sequential, load_model
from keras.layers.core import Dropout, Dense, Activation, Flatten
from keras import optimizers
from statistics import median, mean
from collections import Counter

trainGames = 100000
testGames = 15
trainData = []
scores = []
acceptedScores = []
evalScores = []
choices = []
env = gym.make("CartPole-v0")
env.reset()

def nn_model(inputShape):
    model = Sequential()
    model.add(Dense(32, activation='relu', input_shape=inputShape))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(2, activation='softmax'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
    print(model.summary())
    return model

def create_training_data():
    for i in range(trainGames):
        score = 0
        postStep = []
        lastObs = []
        scoreReq = 100
        done = False
        while not done:
            # choose random action to move left (0) or right (1)
            action = random.randrange(0,2)
            observation, reward, done, info = env.step(action)
            if len(lastObs) > 0:
                postStep.append([lastObs, action])
            lastObs = observation
            score+=reward
        if score >= scoreReq:
            acceptedScores.append(score)
            for step in postStep:
                if step[1] == 1:
                    encodedAction = [0, 1]
                elif step[1] == 0:
                    encodedAction = [1, 0]
                trainData.append([step[0], encodedAction])
        env.reset()
        scores.append(score)    
    return trainData

def train_model(trainData):
    X = np.array([i[0] for i in trainData]).reshape(-1,len(trainData[0][0]),1)
    Y = np.array([i[1] for i in trainData])
    inputShape = (X.shape[1:])
    model = nn_model(inputShape)
    model.fit(X, Y, epochs=5, verbose=1)
    return model

def eval_model(model):
    for i in range(testGames):
        score = 0
        done = False
        lastObs = []
        env.reset()
        while not done:
            env.render()
            if len(lastObs)==0:
                action = random.randrange(0,2)
            else:
                action = np.argmax(model.predict(lastObs.reshape(-1, len(lastObs), 1))[0])
            # Uncomment for random actions instead of predicted ones 
            #action = random.randrange(0,2)
            choices.append(action)    
            observation, reward, done, info = env.step(action)
            lastObs = observation
            score+=reward
        evalScores.append(score)
    
    totalScores = 0
    for x in evalScores:
        totalScores += x
    avgScore = totalScores/len(evalScores)
    print('Average Score: ', avgScore)
    if(avgScore > 190):
        model.save('model_' + str(time.time()) + '_.h5')

if __name__ == '__main__':
    model = None
    try:
        model = load_model('modelNameHere.h5')
    except:
        print('No Available Model to Load')
    if not model:
        trainData = create_training_data()
        model = train_model(trainData)
    eval_model(model)