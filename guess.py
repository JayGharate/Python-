
guess = 0
tries = 0

while guess != 3 and tries < 5:
  guess = int(input('Guess the number:  '))
  tries = tries + 1

if guess != 3:
  print('You ran out of tries.')
else:
  print('You got it!')