import requests 

API_KEY = 'https://api.agify.io/?name='

print("Predict age by name ..")
name = input("Type your name : ") 
response = requests.get(API_KEY+name)
generate = response.json() 
agepredicted = generate["age"]
print("It looks like you are {} years old.".format(agepredicted))

