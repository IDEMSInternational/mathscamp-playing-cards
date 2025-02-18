# Title

Knockdown

# Metadata

## Type

puzzle

# Main Version

## Statement

Pegs numbered 1 to 50 are placed in order in a line, with number 1 on the left.

They are then knocked over, one at a time, following these two rules:

(1.) Starting with the first standing peg on the left, alternate pegs are knocked down, until the end of the row is reached.

(2.) Each time the end of the row is reached, repeat the previous rule.

What is the number of the last peg to be knocked down?

## Correct Answer

32

## Hint

What happens if you only had 5 pegs? What about 10 or 20? Can you spot the pattern?

## Explanation

Start: 1 2 3 4 5 6 7 8 9 ...

First round:  ✕ 2 ✕ 4 ✕ 6 ✕ 8 ✕  ... only even numbers left

Second round: ✕ 4 ✕ 8 ✕ 12 ...  only multiples of 4 left

Third round: ✕ 8 ✕ 16 ✕ 24  ...  only multiples of 8 left

Fourth round: Only multiples of 16 will be left

Fifth round: Only multiples of 32 will be left.

32 is the only multiple of 32 under 50, so 32 is the last peg left.

# Extension 1

## Statement

Pegs numbered 1 to 1050 are placed in order in a line, with number 1 on the left.

They are then knocked over, one at a time, following these two rules:

(1.) Starting with the first standing peg on the left, alternate pegs are knocked down, until the end of the row is reached.

(2.) Each time the end of the row is reached, repeat the previous rule.

What is the number of the last peg to be knocked down?

## Hint

Can you find the closest power of 2 less than 1050?

## Correct Answer

1024

## Explanation

As before, after the first round we have only multiples of 2. The second leaves only multiples of 4, the pattern continues and each subsequent round leaves only multiples of 8, 16, 32, ..., 512, 1024. All of the multiples of 1024 (except 1024 itself) are bigger than 1050, which means 1024 will be the last peg left.

# Extension 2 

## Statement

Pegs numbered 1 to 10000050 are placed in order in a line, with number 1 on the left.

They are then knocked over, one at a time, following these two rules:

(1.) Starting with the first standing peg on the left, this time **9 pegs are knocked down and the tenth is left standing**, until the end of the row is reached.

(2.) Each time the end of the row is reached, repeat the previous rule.

What is the number of the last peg to be knocked down?

## Hint

Think about the sequence of pegs left in the previous parts 2, 4, 8, ... is there another way of writing down this sequence? In what way will the sequence change in this new case?  

## Correct Answer

10000000

## Explanation

This puzzle is similar to the previous parts. In those cases, at each round we left the multiples of the increasing powers of 2. The sequence 2, 4, 8, 16,... can be written 2, 2², 2³, 2⁴,... 

In the new puzzle we have multiples of powers of 10 left. Indeed, after the first round only multiples of 10 are left. After the second round only multiples of 100 = 10² are left, after the third round only leave multiples of 1000 = 10³, and so on. Thus 10000000 = 10⁷ will be the last peg left, as all other multiples of 10⁷ are larger than 10000050.

# Additional information

## About

This puzzle is actually about powers of 2 and binary numbers), and its second extension about powers of 10 and decimal numbers.

## References

* https://nrich.maths.org/11677

