# Symbol Puzzle Solver

I never really liked this puzzle, but there were some in the puzzle book my grandma gave me, and it felt incomplete leaving them blank.

So I figured it would be much more fun to write a quick program to solve them for me!  That's not cheating, right?

## How the puzzle works


You're given an equation, but the symbols are blank:
```
52 _ 4 _ 6 _ 5 = 40
```

And you are told that this equation will be a true statement if you fill in the blanks with 3 out of the following 4 symbols:`+`, `-`, `*`, `/`.  No fractions, or negative numbers are involved.  Also, the left side of the equation will be performed from 'left to right'.  In other words, no Order of Operations are used (wish they'd mentioned that before I read the solution in the back of the book).

My issue with the puzzle is that there isn't really a strategy.  In my mind, I'd be running through every permutation (4p3), which isn't fun.  So when something isn't fun, I like to write a program to do it for me!

Also, I know that the long `if, elif, elif, elif` bit is tedious.  If anyone knows how to avoid this, let me know!
