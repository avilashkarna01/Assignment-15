# Q.1- Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better." Q.3- Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"

import re
email1='Zuck26@facebook.com'
email2='page33@google.com'
email3='jeff42@amazon.com'
print(re.findall(r'(.+)@(.+)\.(.+)',email1),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',email2),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',email3),end="")
print("\n")

# Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter, " \
#        "So she bought some better butter, To make the bitter butter better."

import re
text= "Betty bought a bit of butter, But the butter was so bitter, " \
       "So she bought some better butter, To make the bitter butter better."

p=re.compile(r"[Bb][a-z]+")
result=p.findall(text)
print(result)
print("\n")

# Q.3- Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"
import re
sentence = "A, very very; irregular_sentence"
p=re.sub(r"[^a-zA-Z]"," ",sentence)
print(p)
print("\n")
# Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
p=re.sub(r"! RT @TheNextWeb:"," ",tweet)
p=re.sub(r"http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"," ",p)
print(p)
print("\n")