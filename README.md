SPAM MESSAGE DETECTOR

With today's advance growing world, we are getting more dependent on the internet. We are online most of the time. With great features also comes some risks. My project " SPAM MESSAGE DETECTOR" detects the message as spam or not. My main programming language used in the project is python with use of machine learning models. It uses Naive Bayes Algorithm to classify and TF-IDF for text processing. It also has both GUI AND CLI interfaces and the user can decide if he wants to check the message on terminalor on GUI window.

Video demo :-

Training the model

https://github.com/user-attachments/assets/3ebdbae7-6917-4012-9142-c6efd40a33b1

 CLI INTERFACE ( PREDICTING THE MESSAGE)
 

https://github.com/user-attachments/assets/1419f929-a038-440d-b41d-8d3f282fc5b1

GUI INTERFACE 


https://github.com/user-attachments/assets/c8ece069-9873-4e2f-8f23-c134a0ad3b88

Overview:-

It is made using Machine Learning.

Text data is processed using TF-IDF.

Naive Bayes Algorithm is used for classification.

SMS Spam Message Dataset collection is used and the model is trained on that.

This project allowes you to use two different interface :- Command Line Interface (CLI) and Graphical User Interface (GUI)

Features :-

Detect the spam messages easily.

It is fast

It is easy to use and it is lightweight.

It has CLI interface which tells the results in terminal and can be executed many time.

It also has GUI interface . The GUI window is user-friendly and is very simple.

It uses machine learning.

Technologies used :-

Python (3.13.7)

pandas

scikit-learn

joblib

tkinter

Installations :-

pip install -r requirements.txt

or

py -m pip install -r requirements.txt

How to run the program :-


First step : Training the model

python train.py

Second step : Running the CLI version

python predict.py

( You can execute it a number of times. If you want to stop it just type exit, it will stop )

Third step : Running the GUI version

python gui.py

Input Rules :-

You can enter any text message.

Please avoid empty input.

You can type exit in the CLI to stop the program.

Project Structure :-

train.py used for training the model

predict.py it is the command line for CLI version

gui.py GUI version

requirements.txt python libraries

model.pkl saved trained model

vectorizer.pkl saved TF-IDF

spam.csv dataset of spam messages used for testing and training

Author :-

Priya Ranjan
