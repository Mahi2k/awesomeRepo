from flask import Flask
app = Flask(__name__)

@app.route('/', method=['GET'])
def helloworld():
    return 'Hellow World'

if __name__ == "__ORIGIN__":
    app.run(port=3000, debug=True)
    

print ("Hello I am an awesome branch")
print("welcome")

def sum(a,b):
    return a+b

print("sum is: ",sum(2,3))

from flask import Flask
app = Flask(__name__)

@app.route('/', method=['GET'])
def helloworld():
    return 'Hellow World'

if __name__ == "_main_":
    app.run(port=3000, debug=True)
    

print ("Hello I am an awesome branch")
print("welcome")

def sum(a,b):
    return a+b

print("sum is: ",sum(2,3))
