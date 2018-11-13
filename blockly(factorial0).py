i = None
N = None
result = None

def text_prompt(msg):
  try:
    return input(msg)
  except NameError:
    return input(msg)


N = float(text_prompt('need N '))
if N < 0:
  print('n must be positive')
else:
  i = 0
  result = 1
  for count in range(int(N)):
    i = i + 1
    result = result * i
    print(result)