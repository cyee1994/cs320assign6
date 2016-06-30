CS320 Assignment #6 README
 
This project consists of several python programs that when working together will tokenize the contents of a text file and output their element type.

The first program is a function that takes in a single argument which is the text file to be tokenized. It does this by splitting up the text file by tokens and putting them into a list of lists.

The second program is a set of classes. It consists of a Token class and LiteralIntToken class and a NameToken class. They are meant to be used to organize the tokens from program 1.

The third file takes in a command line arguement that is the text file to be tokenized and uses the first and second program to output the element type of each token in the same format of the original text file. 

prog6_1.py is meant to be used by prog6_3.py

prog6_2.py is meant to be used by prog6_3.py

prog6_3.py is run using ./prog6_3.py x with x being the name of the text file meant to be tokenized.  

