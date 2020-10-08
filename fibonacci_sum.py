def fib(n):
  if n < 2:
    return n
  else:
    # fn = fn-1 + fn-2
    return fib(n-1) + fib(n-2)

def main():
  n = int(input())
  for i in range(n):
    x, y = [int(x) for x in input().split()]
    result = 0
    for j in range(x, y+1):
      result += fib(j)
    print(result)
main()