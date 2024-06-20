# Arithmetic Operators
print("Arithmetic Operators:")
x, y = 10, 5
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} ** {y} = {x ** y}")
print(f"{x} // {y} = {x // y}")
print()

# Assignment Operators
print("Assignment Operators:")
x = 5
print(f"x = {x}")
x += 3
print(f"x += 3 -> {x}")
x -= 3
print(f"x -= 3 -> {x}")
x *= 3
print(f"x *= 3 -> {x}")
x /= 3
print(f"x /= 3 -> {x}")
x %= 3
print(f"x %= 3 -> {x}")
x //= 3
print(f"x //= 3 -> {x}")
x **= 3
print(f"x **= 3 -> {x}")
x &= 3
print(f"x &= 3 -> {x}")
x |= 3
print(f"x |= 3 -> {x}")
x ^= 3
print(f"x ^= 3 -> {x}")
x >>= 3
print(f"x >>= 3 -> {x}")
x <<= 3
print(f"x <<= 3 -> {x}")
x = 5  # Reset x for the next example
print(f"x := {x} -> {x := 3}")
print()

# Comparison Operators
print("Comparison Operators:")
x, y = 5, 10
print(f"x == y -> {x == y}")
print(f"x != y -> {x != y}")
print(f"x > y -> {x > y}")
print(f"x < y -> {x < y}")
print(f"x >= y -> {x >= y}")
print(f"x <= y -> {x <= y}")
print()

# Logical Operators
print("Logical Operators:")
print(f"x < 5 and x < 10 -> {x < 5 and x < 10}")
print(f"x < 5 or x < 10 -> {x < 5 or x < 10}")
print(f"not(x < 5 and x < 10) -> {not(x < 5 and x < 10)}")
print()

# Identity Operators
print("Identity Operators:")
a, b = [1, 2, 3], [1, 2, 3]
c = a
print(f"a is b -> {a is b}")
print(f"a is c -> {a is c}")
print(f"a is not b -> {a is not b}")
print()

# Membership Operators
print("Membership Operators:")
print(f"1 in a -> {1 in a}")
print(f"4 in a -> {4 in a}")
print(f"1 not in a -> {1 not in a}")
print(f"4 not in a -> {4 not in a}")
print()

# Bitwise Operators
print("Bitwise Operators:")
x, y = 5, 3
print(f"x & y -> {x & y}")
print(f"x | y -> {x | y}")
print(f"x ^ y -> {x ^ y}")
print(f"~x -> {~x}")
print(f"x << 2 -> {x << 2}")
print(f"x >> 2 -> {x >> 2}")
print()

# Operator Precedence
print("Operator Precedence:")
print(f"(6 + 3) - (6 + 3) -> {(6 + 3) - (6 + 3)}")
print(f"100 + 5 * 3 -> {100 + 5 * 3}")
print(f"5 + 4 - 7 + 3 -> {5 + 4 - 7 + 3}")
