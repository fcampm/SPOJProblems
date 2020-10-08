n = int(input())
for i in range(n):
  first_number, second_number = input().split()
  first_number = first_number[::-1]
  second_number = second_number[::-1]
  result = int(first_number) + int(second_number)
  result = str(result)
  result = result[::-1]
  result = int(result)
  print(result)
