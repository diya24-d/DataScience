from textblob import TextBlob
y = input("Type your sentence : ")
edu=TextBlob(y)
x=edu.sentiment.polarity

#negtive = x<0 and neutral = 0 and positive x>0 && x<=1
if x<0:
    print("negative")
elif x==0:
    print("neutral")
elif x>0 and x<=1:
    print("positive")

