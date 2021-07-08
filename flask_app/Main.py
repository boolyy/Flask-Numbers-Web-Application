'''
Task:

Create a basic Flask web application:

Root / is not important :)
/<int:number> will display integers from 1 to that number
/<int:number>/odd will display only odd numbers in that range
/<int:number>/even will display only even numbers in that range
/<int:number>/prime will display only prime numbers in that range
 
There are many ways to achieve this, I just want to see how you would approach the problem.

Feel free to show multiple ways but you can also just leave one which is the best in your opinion.

Consider performance and scalability.

This will give us a base to talk about and maybe remove need to ask certain questions entirely.

Extra points for creating a Dockerfile.
'''


import math
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")  # path to get to function
def home():
    return "<h1>Hello! This is the main page!<h1>"


@app.route("/<number>")
def displayIntInOrder(number):

    if (not f"{number}".isdigit()):  # isdigit returns true only for positive integer numbers
        return "<h1>Please enter a positive integer<h1>"

    numInt = int(f"{number}")

    if(numInt == 0):
        return "<h1>There are no numbers for the range you have provided!<h1>"

    returnString = ''
    for i in range(1, numInt + 1):
        returnString = returnString + ' ' + str(i)

    return "<h1>" + returnString + "<h1>"


@app.route("/<number>/odd")
def displayOddInt(number):

    if (not f"{number}".isdigit()):  # isdigit returns true only for positive integer numbers
        return "<h1>Please enter a positive integer<h1>"

    numInt = int(f"{number}")

    if(numInt == 0):
        return "<h1>There are no odd numbers in the range provided!<h1>"

    returnString = ''
    for i in range(1, numInt + 1, 2):
        returnString = returnString + ' ' + str(i)
    return "<h1>" + returnString + "<h1>"


@app.route("/<number>/even")
def displayEvenInt(number):

    if (not f"{number}".isdigit()):  # isdigit returns true only for positive integer numbers
        return "<h1>Please enter a positive integer<h1>"

    numInt = int(f"{number}")

    if(numInt == 1 or numInt == 0):
        return "<h1>There are no even numbers in the range provided!<h1>"

    returnString = ''

    for i in range(2, numInt + 1, 2):
        returnString = returnString + ' ' + str(i)
    return "<h1>" + returnString + "<h1>"


def primeCheck(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if(num % i == 0):
            return False
    return True


@app.route("/<number>/prime")
def displayPrimeInt(number):
    if (not f"{number}".isdigit()):  # isdigit returns true only for positive integer numbers
        return "<h1>Please enter a positive integer<h1>"

    numInt = int(f"{number}")

    if(numInt == 1 or numInt == 0):
        return "<h1>There are no prime numbers in the range provided!<h1>"

    returnString = ''
    for currNum in range(2, numInt + 1):
        if(primeCheck(currNum)):
            returnString = returnString + ' ' + str(currNum)

    return "<h1>" + returnString + "<h1>"


if __name__ == "__main__":
    app.run()
