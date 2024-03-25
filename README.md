# Euclidean Algorithm for Finding Greatest Common Divisor (GCD)

The Euclidean algorithm is an efficient method for finding the Greatest Common Divisor (GCD) of two numbers.

## Algorithm Overview

The algorithm works by iteratively reducing the problem of finding the GCD of two numbers to the problem of finding the GCD of a smaller pair of numbers. It follows these steps:

1. **Step 1: Calculate Remainder**
   - Calculate the remainder `r` when the larger number `a` is divided by the smaller number `b`.

2. **Step 2: Update Values**
   - Update `a` to be the original value of `b`.
   - Update `b` to be the value of the remainder `r`.

3. **Step 3: Repeat (if b != 0)**
   - If `b` is not zero, repeat Steps 1 and 2.

4. **Step 4: GCD (when b = 0)**
   - When `b` becomes zero, the GCD is found, and it's equal to the value of `a`.
