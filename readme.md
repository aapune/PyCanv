**PyCanv 1.0**

**Author: Aniruddha Anikhindi**

**Email: aa.pune@gmail.com**



**PyCanv** is open source console application created using Python

System Requirements: Python 3.6+

Unzip PyCanv.zip to any directory and perform to run PyCanv 
– **cd PyCanv\src** ->**python main.py**


PyCanv is a open source console application created using Python

PyCanv currently supports below basic functions:

1. Create **canvas** in cosole using command : C w h (w=width , h=height)
2. Create **line** in console in canvas range using command : L x1 y1 x2 y2
3. Create **rectangle** in console in canvas range using command :R x1 y1 x2 y2 
4. Bucket fill area in cosole within canvas range using command : B x y <color code>


Along with basic functions it supports below additional features: 
1. Help - using help user can get assistance for any commands requested.

2. Commands are configurable with arguments in config file - commands can be easily replaceable with user needs.

3. If you accidentally trigger create canvas command then user confirmation is requested to keep/delete current canvas or not.
Note: If user confirms Y then previous canvas will be deleted irrespective of new command is correct or not.

4. Lines can be drawn for any valid co-ordinate point where location does not matter.



**PyCanv salient features - How it is build :**

i) PyCanv is developed using Python and all coding standard conventions (PEP 8) and documentation styles are followed.

ii) PyCanv is developed fully using TDD approach - rich set of test cases are available which can be greatly used for reenginerring or development of new modules.

    Canvas creation - 10 test cases
    Line creation - 11 test cases
    Rectangle creation - 8 test cases
    Bucket filling - 18 test cases
    Utils - 9 test cases
    
   Total - **56** test cases which includes normal behaviour, boundary conditions, funtional test cases

   PyTest is used for running testcases
   
   PyTest can be installed by command - **pip install pytest**
   
   Tests can run by - **py.test <testcase_file_name>**
    
    
    
iii) PyCanv software development features:

a) Simple design - PyCanv is developed and designed using simple Python code with no 3rd party libraries.

b) Maintainability - PyCanv is a maintainable framework with easy configuration of various parameters.

c) Testability - PyCanv is having large test case set which can be used for regression or while reengineering.

d) Modularity - PyCanv testing components are designed using modular approach.

g) Error handling - PyCanv handles exceptions and errors and provides appropriate error message to users.

h) Logging - PyCanv uses logging to log user inputs and commands.




