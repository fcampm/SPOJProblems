# Number of the cases that will run.
n = int(input())
for i in range(n):
  starting_index = int(input())
  number = starting_index + 1
  while(True):
    string_number = str(number)
    if (string_number == string_number[::-1]):
      print(int(string_number))
      break
    else:
      number+=1