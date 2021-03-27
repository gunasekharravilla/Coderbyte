# Coderbyte
### Age counting NodeJs

Question 1

Node.js Age Counting
In the JavaScript file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER. Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.

```
Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2
```
<a href="https://github.com/gunasekharravilla/Coderbyte/blob/master/AgeCounting.js">AgeCounting Answer</a>


### Eight Queens 

Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your program should determine if all of the queens are placed in such a way where none of them are attacking each other. If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided. 
For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. The corresponding chessboard of queens for this input is below (taken from Wikipedia). 

![](https://i.imgur.com/zAT24ML.png)

```
Sample Test Cases:
Input:["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]
Output:"(2,1)"
Input:["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]
Output:"(5,3)"
```

<a href="https://github.com/gunasekharravilla/Coderbyte/blob/master/eightqueens.py">Eight Queens Answer</a>
