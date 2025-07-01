
Instructions:
1 Attempt problems given to you .
2 Develop the solution using Python
3 Console interface is enough.
4 Even though these are really small problems, try to write production quality code instead of write-once
and throw kind of code (refactor into small, recognisable modules, use frameworks where needed to save
code, write tests, etc. No need for CI, or scale-out in mind, though.)
5 Please use object oriented design when designing your code.

Problem 2: Game of Life
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is
in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that
are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbours dies, as if by loneliness.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours comes to life.
The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above
rules simultaneously to every cell in the seed - births and deaths happen simultaneously, and the discrete
moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of
the one before.) The rules continue to be applied repeatedly to create further generations.
Problem:
The below inputs provide the pattern or initial cells in the universe, especially their (x,y) co-ordinates. The
output is the state of the system in the next tick (one run of the application of all the rules) , represented in the
same format - i.e. x,y coordinates of all the alive cells after one tick.
------------------------------------------------------------------------------------------------------------------
Input A:
(Block pattern - Still life)
1, 1
1, 2
2, 1
2, 2
Output A:
1, 1
1, 2
2, 1
2, 2
--------------------------------------------------------------------------------------------- ---------------------
Input B
(Boat pattern - Still life)
0, 1
1, 0
2, 1
0, 2
1, 2
Output B
0, 1
1, 0
2, 1
0, 2
1, 2
--------------------------------------------------------------------------------------------- ---------------------
Input C
(Blinker pattern - oscillator)
1, 1
1, 0
1, 2
Output C
1, 1
0, 1
2, 1
--------------------------------------------------------------------------------------------- ---------------------
Input D
(Toad pattern - two phase oscillator)
1, 1
1, 2
1, 3
2, 2
2, 3
2, 4
Output D
0, 2
1, 1
1, 4
2, 1
2, 4
3, 3
==========