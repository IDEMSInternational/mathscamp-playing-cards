# Title

Sword of Josephus

# Metadata

## Type

puzzle

# Main Version

## Statement

Pegs numbered 1 to 52 are placed in a circle. Starting with number 2, alternate pegs are knocked down until only one is left.

What is the number of the last peg to be knocked down?

## Correct Answer

41

## Hint

What happens if you only had 2 pegs? What about 3, 4, 5, 6, 7, or 8 pegs? Can you spot the pattern after considering these cases?

## Explanation

Starting with only 2 pegs, we know that the last peg to be knocked down would be number 1. We can work out which would be the last peg if we increase the number of pegs. To start, we record our results and look for a pattern.

2 - 1

3 - 3

4 - 1

5 - 3

6 - 5

7 - 7

8 - 1

9 - 3

And so on. Each power of two (1, 2, 4, 8, …) "resets" the last peg standing to be number 1. You can see that the number of the last peg standing goes up in odd numbers after this. To work out the answer for 52, we know the last reset was the largest power of two. The largest power of two below 52 is 32, and 52 - 32 = 20. So it is the twentieth odd number that is calculated as 2×20 + 1 = 41.  

# Extension 1

## Statement

Pegs numbered 1 to 2000 are placed in a circle. Starting with number 2, alternate pegs are knocked down until only one is left.

What is the number of the last peg to be knocked down?

## Hint

What is the biggest power of 2 (1, 2, 4, 8, ...) that is less than 2000?

## Correct Answer

1953

## Explanation

The biggest power of 2 below 2000 is 1024. As 2000 - 1024 = 976, the final peg will be the 976ᵗʰ odd number, 976×2 + 1 = 1953.

# Additional information

## About

The legend of this puzzle is about a group of soldiers in a circle. 

## References

* https://lycee.samicharity.co.uk/2016/10/20/sword-of-josephus/

