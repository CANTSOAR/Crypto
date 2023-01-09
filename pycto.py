import math
import numpy as np
from PIL import Image

alpha = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def alphatobase10(input):
  base10num = 0
  input = preptext(input)
  for letter in range(len(input)):
    base10num += alpha.index(input[letter]) * len(alpha) ** letter

  return base10num

def base10to255array(number):
  base255 = []

  power = int(math.log(number, 255))
  iterator = 0
  
  while power - iterator + 1:
    base255.append(int(number / 255 ** (power - iterator)))
    number = number % 255 ** (power - iterator)
    iterator += 1

  for x in range(2 - power):
    base255 = [0] + base255

  return base255

def base10to255cubed(number):
  base255cubed = []

  power = int(math.log(number, 16581375))
  iterator = 0
  
  while power - iterator + 1:
    base255cubed.append(int(number / 16581375 ** (power - iterator)))
    number = number % 16581375 ** (power - iterator)
    iterator += 1

  return base255cubed

def makeimagefrom255cubed(inputarray):
  print(len(inputarray), "pixels of data available")
  height = int(input("image height? "))
  width = int(input("image width? "))
  name = input("name to save img as? ")
  
  image = np.zeros([height, width, 3], dtype=np.uint8)

  h = 0
  w = 0
  
  for num in inputarray:
    if h == height:
      print("image size too small, try larger")
      return
    image[h][w] = base10to255array(num)
    w += 1
    if w == width:
      w = 0
      h += 1

  img = Image.fromarray(image)
  img.save(name + ".png")
  
def encodetoimage():
  original = input("something: ")
  
  base10number = alphatobase10(original) #alpha --> normal nums
  base255cubedarray = base10to255cubed(base10number) #to big number
  makeimagefrom255cubed(base255cubedarray) #make image

def decodefromimage():
  image = input("which image do you want to open: ")
  img = Image.open(image)
  array = np.array(img)[:,:,:3]
  
  number = cubedarraytobase10(array)
  decoded = base10toalpha(number)
  print(decoded)
  
def cubedarraytobase10(array):
  array = array.reshape(-1, 3).tolist()
  j = 1
  while not sum(array[-j]):
    j += 1

  i = len(array) - j
  
  number = 0
  power = i
  
  while i + 1:
    number += (array[i][0] * 255 ** 2 + array[i][1] * 255 + array[i][2]) * 16581375 ** (power - i)
    i -= 1

  return number

def base10toalpha(number):
  chars = []

  power = int(math.log(number, len(alpha)))
  iterator = 0
  
  while number:
    chars.append(int(number / len(alpha) ** (power - iterator)))
    number = number % len(alpha) ** (power - iterator)
    iterator += 1

  decoded = ""

  for char in chars:
    decoded = alpha[char] + decoded

  return decoded

def preptext(text):
  #text = text.lower()
  for char in text:
    if char not in alpha:
      text = text.replace(char, "")

  return text


run = True
while run:
  do = input("what do encode, decode or quit: ")
  if do == "encode":  
    encodetoimage()
  elif do == "decode":
    decodefromimage()
  elif do == "quit":
    run = False
  else:
    print("only encode, decode, or quit")