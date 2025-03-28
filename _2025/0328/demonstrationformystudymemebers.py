import sys

print("read a string!")
str1 = sys.stdin.readline()
print("*****")
print(str1)
print("*****")
print()

print("read a integer!")
int1 = int(sys.stdin.readline())
print("*****")
print(int1)
print("*****")
print()

print("don't cast a integer!")
int1 = (sys.stdin.readline())
print("*****")
print(int1)
print("*****")
print()

print("strip() a string!")
str1 = sys.stdin.readline().strip()
print("*****")
print(str1)
print("*****")