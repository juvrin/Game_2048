# Game 2048

Game 2048 is a terminal version of the 2048 game where you swipe tiles to sum them.
The game is finished when you've either got a tile with 2048 on it or if you cannot
move any tiles.

<img src="/screenshot.png" alt="Screenshot of 2048 game" width="261" height="277">


## Getting started

Download the repository to your computer. Use the "w" (up), "s" (down), "a" (left) and
"d" (right) keys to swipe the grid.


## How It's Made

This game was made in Python 3.13.7. There are very few modules used to run this game. The most
fancy thing is some ASCII art I added at the beginning and end of the game.
I was struggling with the tile moving logic and keeping the code succint.
In the end, I settled for rotating the grid BEFORE the tiles are moved and rotating it back again
AFTER the tiles have been moved. This way I only needed 1 function to move the tiles. 
Tiles are always moved up. For example, in order to move tiles 
to the left, the entire grid is rotated 90 degrees to the right (clockwise). 
Tiles are then moved upwards and the grid is rotated back 90 degrees counterclockwise.

Another challenge was making sure that previously summed tiles are not summed again. 
Let me use an example to explain this. Suppose you have a 4 in the third row
and above that a 2 in the second row and above that another 2 in the top row.
In the move_cells function, we loop over the grid from left to right, top to bottom.
This means that the 2 in the second row will first be added to the 2 in the top row.
So now you have a 4 in the top row and still your 4 in the third row. 
In a previous (and wrong) iteration of my script, the logic would then continue to 
sum the 4 in the third row to my new 4 in the top row. 
But this is not what happens in the original game. So I had to change this.
In the end, I opted for adding a placeholder "X" on the row below the result of the sum. 
In the example, this would mean there would be an "X" placed in the second row.
When moving the 4 in the third row, this "X" is taken into consideration.
This way, I could ensure that newly created sums/tiles are not being summed twice in the same swipe.

## Roadmap

- Add a graphical interface with pygame

## Contact

Jules Vrinten https://www.linkedin.com/in/jules-vrinten/ 
https://github.com/juvrin


## License

[MIT](https://choosealicense.com/licenses/mit/)