# 3 Levels Of Calculator Homework

For this homework. what you need to do is to try to make the most complete calculator that can add, subtract, multiply, divide and store a history of calulations.  The purpose of this assignment is to introduce you understand the principles of object oriented programming, unit testing, and design principles such as SOLID, DRY, GRASP, and Seperation of concerns.  Its important to understand how to properly organize your code using the professional "grammer" of programming and not just the syntax of if statements and loops.

## Submission Instructions
1.  Make a new repo from scratch and set it up like last time, so you can run pytest, pylint, and coverage.  You could even start with a copy of your last repo.

2.  Submit a link to your repository to Canvas when your finished.

## To get my code to run / Install Instructions

1.  Clone the repo
2.  CD into the repo directory
3.  Create the virtual environment
4.  Activate the virtual environment
5.  Install the requirements with pip or pip3 install requirements.txt

**NOTE: YOU NEED TO CHECKOUT BRANCH "PART3" TO SEE THE DETAILED CODE COMMENTS**

Basic tips:
* Don't repeat yourslf #1 rule
* Separate each thing the program needs to do, so its organized and your functions only do one thing


You should create new branches for each version of your progarm and work from the most simple, which is the first branch (main) and then keep upgrading your program until you have all of the requirements met.  Please don't just copy and paste my final program, or you will not learn anything.  Soon you will have to design your own program without any examples, which will be your mid-term.  I have commented the code with explanations, so you can understand it better.   

In this repository, you can see that there are 3 branches:

1.  Main - Basic Calculator with functions
2.  Part 2 - Intermediate Calculator with static methods on Calculator class and instance methods on Calculation class to perform operations on the data in the calculation instance.
3.  Part 3 - Advanced Calculator **Has the detailed comments to read**

## Instructor Video and Required Readings

1.  Instructor Video - [here](https://youtu.be/YrtBikBdZOE)
2.  Concept Explanatinos - [here](oopconcepts.md)

## Notes on Advanced Calculator
The advanced calculator in part 3 contains static methods on the Calculator, instance methods on the Calculation, and class methods on the Calculations class.  In addition, it has more advanced testing that uses parameterized test data and a fixture to make it easy to setup each test with consistent data.  There are also modifciations to the .pylintrc file to control pylint's code analysis and I disable pylint errors in the calculator/calculation.py file by putting this code at the top of the file, which you can also use inside a specific function to disable a pylint check for a specific file.   You sometimes need to disable pylint when you know you are doing the correct thing, but that for some reason pylint doesn't understand.  It's better to disable it at the function or file level than the global level because you never know when you really do want it to tell you the style error.

**"# pylint: disable=unnecessary-dunder-call, invalid-name"**


## The objective of this homework assignment is to create your own 

Your goal in this homeowrk is to design your own calculator from scratch using the techniuqes that you can figure out based on my examples.  Your calculator needs to do the following:

1. Add, Subtract, Multiply, and Divide
2. Throw exception for divide by zero and test that the exception is thrown
3. Use at least one class, at least one static method, at least one class method.
4. It needs to  store a history of calculations, so that you can retrieve the last calculation, add a calculation, 
5. It needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code.  
6.  You should use type hints for input parameter types and return types.
7.  Implement a pytest fixture to test the 

## Grading:

1.  20  Points for (add subtract, multiply, divide) 
2.  10 Points for exception throwing and testing on divide by zero
3.  30 points each for using static, class, and instance methods correctly
4.  5 Points for having a calculation class that stores the arthitmentic operation in a instance property.
5.  15 Points for having a calculation history to store calculation instances
6.  10 Points for having the convenience methods on the calculations class to manage the history
7.  10 Points for using parameterized test data