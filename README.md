<h1>Connect Four the game</h1>

<h2>Description</h2>
Well-known connect four game.
You get 4 (or more.. yes you get style points for more) symbols of same colour in row/column/diagonal -> You Win!
<br />

<h2>Languages and Utilities Used</h2>
- <b>Python</b> 
- <b>Python tkinter</b>

<h2>Program walk-through:</h2>
I gave the game a really simple UI, made in tkinter.
The code is decomposed into:
- draw_board.py (which draws the board, and all other stuff)
- check.py (which checks If a player with last move is a winner)
- connect_four_game.py (runs the game, keeps the scoreboard, shows who's turn it is)
- tests-check.py (checks basic occurences [but the majority of testing was done by playing the game] )

<p align="center">
The UI<br/>
<img src="https://i.imgur.com/mNpZlf6.png" height="80%" width="80%" />
<br />
<br />
Score, who's turn<br/>
<img src="https://i.imgur.com/hf6qPq2.png" height="80%" width="80%" />
<br />
<br />
You can place as much as you want(as long as your spacebar works)<br/>
<img src="https://i.imgur.com/FrY8ZJR.png" height="80%" width="80%" />
<br />
<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
