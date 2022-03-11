# Title

Square numbers and triangular numbers

# Metadata

## Type

Fun fact

# Main Version

## Statement

The first five triangular numbers are 1, 3, 6, 10, and 15

The first five square numbers are 1, 4, 9, 16, and 25

Any square number bigger than 1 is the sum of two consecutive triangular numbers.

## Hint

Triangular numbers can be drawn with dots in the shape of a triangle. Square numbers can be drawn with dots in the shape of a square grid. See if you can work this one out visually first. Can you express it algebraically as well?

## Explanation

We first show this visually, in the image below you can see that 4 = 1 + 3,  9 = 3 + 6, 16 = 6 + 10, and 25 = 10 + 15. 

![](Square%20Numbers%20and%20Triangular%20Numbers_images/image_0.png)

If we take T = triangular and S = square, then we can draw the S-number as an S-grid of points, the smaller T-number forms the upper T of points, the larger T-number forms the lower T AND the diagonal of points.

These are consecutive triangular numbers making a square.

The side length in points of the bigger T-number is the square root of the S-number. 

# Extension 1

## Statement

Find the 250ᵗʰ triangular number.

## Hint

Starting with a small triangular number might help. Can you use the pattern of triangles and squares to help you? What square could be the sum of the 250ᵗʰ triangular number and another triangular number? Think about the 250ᵗʰ square number and how it relates to the 250ᵗʰ triangular number.

## Explanation

Let us look at a smaller example first. We could find the 5ᵗʰ triangular number using this square:

![](Square%20Numbers%20and%20Triangular%20Numbers_images/image_1.png)

We are looking for the number of purple squares. We can do ½×(5×5 - 5) = 10 to get the pink triangle. And then adding on the 5 squares in the diagonal gives the purple triangle. So we have 15.

![](Square%20Numbers%20and%20Triangular%20Numbers_images/image_2.png)

For the 250ᵗʰ triangular number, we are looking for the number of squares in the black "triangle". It will be roughly ½×250×250, except that the diagonal will be included. So we calculate ½×(250×250 - 5) to find the blue triangle and then add 250 on to find the black triangle. The answer is 31375.

We can extend this logic to find a formula for the nth triangular number

½×(n×n - n) + n = ½×(n² +2×n - n) = ½×(n² + n) = ½×n×(n + 1)

Check: ½×250×251 = 31375

Using the formula, we can also see that consecutive triangular numbers add to a square number. Consecutive triangular numbers can be represented as ½×(n - 1)×n and ½×n×(n + 1).

If we add these consecutive triangular numbers and simplify we can find:

 ½×(n - 1)×n + ½×n×(n + 1)=  ½×((n - 1)×n + n×(n + 1)) = ½×(n² - n + n²  + n) = n² 

# Additional information

## About

The formula for the nᵗʰ triangular number is also exactly equal to the summation 1 + 2 + 3 + … + n and so it is a quick way to add up lists of consecutive numbers! This formula was written down by the Irish monk Dicuil in about 816AD but was possibly already known to the Pythagoreans in the 5th century BC.

## References

* https://www.geogebra.org/m/ZXAP0QPv

* https://nrich.maths.org/2274

* https://en.wikipedia.org/wiki/Triangular_number#Applications

