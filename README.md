Gagan Heer

COMP 8901

Repo: https://github.com/GaganHeer/AI_Projects

## Python Projects (Available on GitHub):
- The python files are built to work on Linux and OSX
- You need to have python3 installed in order to run these projects
- below are the commands to quickly setup python3 if not already installed (do these on the terminal):
- 1) xcode-select --install
- 2) ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- 3) export PATH="/usr/local/opt/python/libexec/bin:$PATH"
- 4) brew install python
- 5) sudo easy_install pip

After python3 is installed please enter the file directory of the project you which to access and then install the requirements from the requirements.txt file 
- 6) cd [directory of mini project]
- 7) pip install -r requirements.txt

### Rule Based - Blackjack
- This Python project uses the OpenAI Gym library for creating the game environment. 
- The OpenAI Gym library only supports Linux and OSX environments at the moment.
- If you'd like to perform random actions instead of rule based ones you can uncomment line #51 and #73

### Ngrams Action Prediction - Rock Paper Scissors
- If you'd like to perform random actions instead of n-grams based ones you can uncomment line #61

### Artificial Neural Network - Cartpole
- This Python project uses the OpenAI Gym library for creating the game environment. 
- The OpenAI Gym library only supports Linux and OSX environments at the moment. 
- I've included a trained model that can be used by changing the value of line #109 to 'bestModel.h5' instead of 'modelNameHere.h5' else it will create and train a new model. 
- If rendering the environment is an issue then you can comment out the 'env.render()' function found at line #85 of the file.
- If you'd like to perform random actions instead of neural network prediction based ones you can uncomment line #91



## C# Unity Projects (Zipped up .exe in folder and available on GitHub):
- The Unity files were built using version 2019.1.4f1

### State Machine - Get Past the Guard
- This project is built using Unity and C#
- It can be run by launching the A00933997_runnable_project_StateMachine.exe file (inside StateMachine folder)

### Seek And Flee - Tag
- This project is built using Unity and C#
- It can be run by launching the A00933997_runnable_project_SeekAndFlee.exe file (inside SeekAndFlee folder)
- If you’d like player 1 to automatically move by itself you can uncomment line #47-50 and #69-71
