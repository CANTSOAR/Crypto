alpha = " abcdefghijklmnopqrstuvwxyz"

def dec_to_vars(dec_input):
  """a = 1
  b = 1

  while a / b != dec_input:
      if (((a + 1) / b - dec_input) ** 2) ** (1/2) < ((a / (b + 1) - dec_input) ** 2) ** (1/2):
          a += 1
      else:
          b += 1"""

  a = 1 - 1 / (1 + dec_input)
  b = 1 / (1 + dec_input)

  print("a is", a, "b is", b, a / b)

def alphatobase10(input):
  base10num = 0
  input = preptext(input)
  for letter in range(len(input)):
    base10num += alpha.index(input[letter]) * 27 ** letter

  return base10num 

def preptext(text):
  #text = text.lower()
  for char in text:
    if char not in alpha:
      text = text.replace(char, "")
  return text

def todecimal(num):
  numstring = str(num)
  numstring = "." + numstring
  dec = float(numstring)
  return dec

text = input("Something: ")
numtext = alphatobase10(text)
decimal = todecimal(numtext)
print(text, numtext, decimal)
dec_to_vars(decimal)