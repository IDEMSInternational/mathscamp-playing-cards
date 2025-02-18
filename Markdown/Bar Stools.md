# Title

Bar Stools

# Metadata

## Type

counting

# Main Version

## Statement

How many different ways can you arrange teachers and students in a row of 5 chairs such that no 2 teachers are sat next to each other?

## Correct Answer

13

## Hint

You could have five students sitting on the five chairs. You could have two teachers sitting on chairs number 2 and 4 and students in chairs 1, 3, and 5. Can you think of any other options? Can you think of the maximum number of teachers that could sit on the chairs? You might like to start with a smaller number of chairs and work your way up.

## Explanation

Think of chairs as having a teacher (x) or a student (o).

For 5 chairs we can have

ooooo, xoooo, oxooo, ooxoo, oooxo, oooox, xoxoo, xooxo, xooox, oxoxo, oxoox, ooxox, xoxox

Total = 13

There is a way we can build up to this solution by thinking about the answer if there was 1 chair, 2 chairs, 3 chairs etc. 

1 chair has 2 options: x , o

2 chairs has 3 options: ox, oo, xo

3 chairs has 5 options: oox, ooo, oxo, xox, xoo

Each time you add a chair you can generate the new options by simply adding a student to the start of all the previous options. You can also add a teacher and then a student to all of the options from two chairs ago. Let's see this with 4 chairs:

Add o onto all the 3 chair options gives:

ooox, oooo, ooxo, oxox, oxoo

And adding xo onto all the 2 chair options gives:

xoox, xooo, xoxo

This gives 5 + 3 = 8 options in total. 

For the 5 chairs we can add o onto all the 4 chairs options and and xo onto all the 3 chair options which gives 8 + 5 = 13 as before.

# Extension 1

## Statement

How many different ways can you arrange teachers and students in a row of 10 chairs such that no 2 teachers are sat next to each other?

## Hint

Try and build up the answer from a smaller number of chairs.

## Correct Answer

144

## Explanation

We had already found the following sequence for 1 chair, 2 chairs, 3 chairs , … 

2, 3, 5, 8, 13

Each term in the sequence can be found by adding the two previous terms. We can carry it on:

2, 3, 5, 8, 13, 21, 34, 55, 89, 144

So there are 144 ways to have people sitting on the 10 chairs.

# Extension 2

## Statement

For all the number of chairs between 1 and 30 inclusive, how many of these will have an even number of ways of sitting on them?

## Hint

Think about how the sequence is generated … can you find a pattern that repeats thinking about odd and even numbers?

## Correct Answer

10

## Explanation

For the sequence 2,3,5,8,13, … we can see that there is a pattern even, odd, odd, even, odd odd, etc. This makes sense as even + odd = odd and odd + odd = even. So every third number in the sequence is even. We need to do 30 ∕ 3 = 10. 

# Additional information

## About

The sequence of numbers in this puzzle are part of the Fibonacci Sequence sequence: 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34,... It is easy to find the next number by adding the previous two numbers, but you can also find the nᵗʰ Fibonacci number in the sequence directly using this formula:

\[$$F_n = \frac{1}{\sqrt{5}}\left[ \left(\frac{1+\sqrt{5}}{2}\right)^{n+1} - \left(\frac{1-\sqrt{5}}{2}\right)^{n+1}\right]$$\]\< Fₙ = (1 ∕ √5)×( ((1 + √5) ∕ 2)ⁿ⁺¹ - ((1 - √5) ∕ 2)ⁿ⁺¹ ) \>

## References

* http://datagenetics.com/blog/june52020/index.html

* http://datagenetics.com/blog/october22015/index.html

* https://www.mathsisfun.com/numbers/fibonacci-sequence.html

