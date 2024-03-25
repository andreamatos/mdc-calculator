def gcd(a, b):
    # Calculate the remainder of 'a' divided by 'b'
    remainder = a % b

    # Store the current value of 'b' in a temporary variable
    temp_b = b

    # Update the value of 'b' with the value of the remainder
    b = remainder

    # Update the value of 'a' with the original value of 'b'
    a = temp_b

    # Repeat the process until 'b' becomes 0
    while b != 0:
        # Calculate the remainder of 'a' divided by 'b'
        remainder = a % b

        # Store the current value of 'b' in a temporary variable
        temp_b = b

        # Update the value of 'b' with the value of the remainder
        b = remainder

        # Update the value of 'a' with the original value of 'b'
        a = temp_b

    # Return the GCD, which is stored in 'a'
    return a


# Example usage:
result = gcd(24, 36)
print("GCD:", result)