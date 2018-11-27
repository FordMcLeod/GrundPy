# GrundPy
A simple recursive solver with memoization for Grundy's Game. 
# The game
Grundy's game is a two-player mathematical game of strategy. The starting configuration is a single heap of objects, and the two players take turn splitting a single heap into two heaps of different sizes. The game ends when only heaps of size two and smaller remain, none of which can be split unequally. The game is usually played as a normal play game, which means that the last person who can make an allowed move wins. 
# Illustration
A normal play game starting with a single heap of 8 is a win for the first player provided he does start by splitting the heap into heaps of 7 and 1: 
  player 1: 8 → 7+1
Player 2 now has three choices: splitting the 7-heap into 6 + 1, 5 + 2, or 4 + 3. In each of these cases, player 1 can ensure that on the next move he hands back to his opponent a heap of size 4 plus heaps of size 2 and smaller: 
  player 2: 7+1   → 6+1+1        player 2: 7+1   → 5+2+1        player 2: 7+1   → 4+3+1
  player 1: 6+1+1 → 4+2+1+1      player 1: 5+2+1 → 4+1+2+1      player 1: 4+3+1 → 4+2+1+1
Now player 2 has to split the 4-heap into 3 + 1, and player 1 subsequently splits the 3-heap into 2 + 1: 
  player 2: 4+2+1+1   → 3+1+2+1+1
  player 1: 3+1+2+1+1 → 2+1+1+2+1+1
  player 2 has no moves left and loses
# Future directions:
* Compare perfomance of Hayward's nim solvers to my Grundys game solver using the Sprague-Grundy theorem which states that there is an ismorphic mapping from a Grundy's Game game is equivalent to a nimber **(this extends to ANY impartial game under the normal play convention) **.  state to a Nim Heap game state
* Make a faster solver that just maps to the corresponding Nim state and utilize the nim-sum 
## Credit to wikipedia for the game description and illustration sections. 
