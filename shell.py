#Shell to run PhCode Commands

from commands import *

def start():
  name = input('>>> ')
  if name == '':
      name = 'main.ph'
  return name

try:
    send_(start())
    ask_(start())  
except:
    pass    