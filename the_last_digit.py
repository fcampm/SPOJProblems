n = int(input())
for i in range(n):
  x, y = [int(x) for x in input().split()]
  result = x ** y
  result = result % 10
  print(result)
