# predict.py 

import joblib

# Load model and vectorizer 


model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")



print("Spam Messagr detector is working , just a little time.  (type 'exit' to stop whenever you want)\n")



#Conditions for spam detecting messages 


while True:
    msg = input("Enter message: ")

    if msg.lower() == "exit":
        print("I was glad to help you. Byee !!")
        break



    vec = vectorizer.transform([msg])
    result = model.predict(vec)[0]



# what to print about messages 


    if result == 1:
        print("Spam, risky do not believe this message.\n")
    else:
        print("Not Spam, you can go forward. \n")


# end of predict

