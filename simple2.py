alpha = [" ","a","b","c","d",
         "e","f","g","h","i",
         "j","k","l","m","n",
         "o","p","q","r","s",
         "t","u","v","w","x",
         "y","z"]

def encode(original = ""):
  if not original:
    original = input("input: ")
  encoded = ""
  shift = 3
  for char in original.lower():
    encoded += alpha[(alpha.index(char) + shift) % len(alpha)]
    shift = alpha.index(char)

  print("Encoded: ", encoded)
  return encoded

def decode(encoded = ""):
  if not encoded:
    encoded = input("input: ")
  original = ""
  shift = 3
  for char in encoded.lower():
    original += alpha[(alpha.index(char) - shift) % len(alpha)]
    shift = alpha.index(original[-1])

  print("Decoded: ", original)
  return original

encoded = encode()
decode(encoded)