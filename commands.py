# Commands for PhCode

import math


_send = 'send('
_ask = 'ask('

def send_(file):
 if _send in file:
  text_quarter = file.partition(_send)[2]
  text_half = text_quarter.replace("'", "")
  text_three = text_half.replace(";", "")
  final_text = text_three.replace(")", "")
  print(final_text)

def ask_(file):
 if _ask in file:
  ask_quarter = file.partition(_ask)[2]
  ask_half = ask_quarter.replace("'", "")
  ask_three = ask_half.replace(";", "")
  final_ask = ask_three.replace(")", "")
  input(final_ask)

    
 

    

