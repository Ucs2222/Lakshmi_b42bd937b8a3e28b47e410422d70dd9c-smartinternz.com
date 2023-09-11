def recurFact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * recurFact(n - 1)


number = int(input("Enter the number :"))
res = recurFact(number)
print(
    "The Factorial of ",
    number,
    " is ",
    res,
)
