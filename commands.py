# Commands for PhCode

import math
import json


_send = 'send('
_ask = 'ask('
string = 'str '
var_identify = '`'

variables = []

def str_(file):
  if string in file:
    str_half = file.partition(string)[2]
    name = str_half.split()[0]
    vstring = str_half.split()[2]
    vwrite = {name: vstring}
    variables.append(vwrite)

def send_(file):
 if _send in file:
  text_quarter = file.partition(_send)[2]
  text_half = text_quarter.replace(";", "")
  text_three = text_half.replace(")", "")
  if var_identify in file:
   var_name = text_three.replace("`", "")
   var_string = variables[0][var_name].replace("'", "")
   print(var_string)
  else:
   final_text = text_quarter.replace("'", "")
   print(final_text)

def ask_(file):
 if _ask in file:
  ask_quarter = file.partition(_ask)[2]
  ask_half = ask_quarter.replace("'", "")
  ask_three = ask_half.replace(";", "")
  final_ask = ask_three.replace(")", "")
  input(final_ask)


    
 

    

