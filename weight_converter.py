weight = input("Weight: ")
unit = input ("(K)kg or (l)ps ")

if unit =="K":
      converter = int(weight) / 0.45
      print(converter)
else:
      converter = int (weight) * 0.45
      print(converter)