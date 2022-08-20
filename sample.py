from re import A


x = 10
y = 5
# Arithmatic operators
print(x+y)  # 10+5
print(x-y)  # 10-5
print(x*y)  # 10*5
print(x/y)  # 10/5
print(x % y)  # reminder of 10/5
print(x**y)  # 10x10x10x10x10
print(x//y)  # gives the nearest whole number of quotient
# Assignment operator
a = 5
print(a)
a += 3
print(a)
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)
a %= 3
print(a)
a //= 3
print(a)
a **= 3
print(a)

# Comparison operator
a = 6
b = 7
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
# Identity Operators
# is
# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is not y)
print(x == y)
# Logical Operator
a = 5
b = 6
c = 5
print(a > b and a == 5)
print(a < b or a == 5)
print(not (a > b and a == 5))
# python Membership
x = ["apple", "banana"]
print("apple" in x)
print("banana" not in x)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
