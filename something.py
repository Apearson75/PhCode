import math


def start():
  name = input('>>> ')
  if name == '':
      name = 'main.ph'
  return name

_send = 'send('
_ask = 'ask('

code = open(start(), 'r')
text = code.read()

flag = 0
index = 0

if _send in text:
  text_quarter = text.partition(_send)[2]
  text_half = text_quarter.replace("'", "")
  text_three = text_half.replace(";", "")
  final_text = text_three.replace(")", "")
  print(final_text)

if _ask in text:
  ask_quarter = text.partition(_ask)[2]
  ask_half = ask_quarter.replace("'", "")
  ask_three = ask_half.replace(";", "")
  final_ask = ask_three.replace(")", "")
  input(final_ask)

    
 

code.close()    

