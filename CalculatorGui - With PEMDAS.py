''' #Jonathan G. '''

from Tkinter import *
from functools import partial
import __future__
import math

'''
special changes: 

1. if result is an integer it will be displayed as an integer (and not as a float like: 5.0).
2. window is not resizable because resizing it makes buttons' sizes be out of proportion.
3. font is bigger to make things readable.
4. if '=' button was pressed, the next button will clear the label and will be displayed.
5. PI and euler's number added.

'''
'''
grid looks like this:

1 2 3 + ^
4 5 6 - .
7 8 9 * C
0 = A / D

'''

calc = Tk()
calc.geometry('500x500+200+200')
calc.resizable(False, False)
calc.title('Calculator')

b_frame = Frame(calc, relief = SUNKEN)
b_frame.pack(side = BOTTOM)
dbh = 2 # default_button_height
dbw = 5 # default_button_width
ans = 0.0
equ_pressed = False # check if last button pressed is '=' button


def Compute_Input(text):        # computes the value of an equation in given string
   
   text = text.replace('^','**').replace('PI','math.pi').replace('e','math.e')
   compute = lambda m: eval(compile(m, '<string>', 'eval', __future__.division.compiler_flag))   # 'eval' function evaluates string that contains a math expression
   global ans

   try:
      result = compute(text)

   except Exception as exc:
      if type(exc) is ZeroDivisionError:
         result = 'Math Error'
      else:
         result = 'Syntax Error'

   else:
      ans = result

   return result


def Pressed(button):    # changes text according to pressed button

   button = str(button)
   new_text = ''   
   global equ_pressed

   calc_line.configure(text = '') if equ_pressed else None
   
   if button not in ['C', 'DEL', '=', 'ANS']:
      new_text = calc_line.cget('text') + button

   elif button == '=':
      rta = Compute_Input(calc_line.cget('text'))  # result to append
      new_text = str(int(rta) if int(rta) == rta else rta) if rta not in ['Syntax Error', 'Math Error'] else str(rta)
      equ_pressed = True
      calc_line.configure(text = new_text)
      return None

   elif button == 'ANS':
      new_text = calc_line.cget('text') + str(int(ans) if int(ans) == ans else ans)

   elif button == 'DEL':
      new_text = calc_line.cget('text')[:-1]

   else:
      pass

   equ_pressed = False
   calc_line.configure(text = new_text)


def Place_Buttons():
   
   num_buttons = {}
   op_buttons = {}
   util_buttons = {}
   br_spe_buttons = {}
   ops = ['+', '*', '-', '/', '^', '.']
   braces = ['(', ')']
   utils = ['C', 'DEL']
   special = ['ANS', '=']
   

   # number buttons from 0 to 9
   for i in range(10):
      num_buttons[i] = Button(b_frame, text = str(i), fg = 'blue', width = dbw, height = dbh, font = (None,14), command = partial(Pressed, i))

   # place number_buttons
   num_buttons[0].grid(row = 3, column = 0)
   for i in range(1,10):
       num_buttons[i].grid(row = (i - 1) / 3, column = (i - 1) % 3)

   # op buttons
   for op in ops:
       op_buttons[op] = Button(b_frame, text = str(op), fg = 'red', width = dbw, height = dbh, font = (None,14), command = partial(Pressed, op))

   tmp_index = 0
   # place op buttons
   for i in range(3):
      for j in [3,4]:
         op_buttons[ops[tmp_index]].grid(row = i, column = j)
         tmp_index += 1

   tmp_index = 0
   # create and place braces buttons and special buttons 
   for symb in (special + braces):
      color = 'darkgreen' if symb in special else 'red'
      br_spe_buttons[symb] = Button(b_frame, text = str(symb), fg = color, width = dbw, height = dbh, font = (None, 14), command = partial(Pressed, symb))
      br_spe_buttons[symb].grid(row = 3, column = 1 + tmp_index)
      tmp_index += 1

   tmp_index = 0
   # create and place utility buttons
   for util in utils:
      util_buttons[util] = Button(b_frame, text = str(util), fg = 'darkblue', width = dbw, height = dbh, font = (None, 14), command = partial(Pressed, util))
      util_buttons[util].grid(row = tmp_index, column = 5)
      tmp_index += 1

   # pi button
   pi_button = Button(b_frame, text = u'\u03C0', fg = 'blue', width = dbw, height = dbh, font = (None, 14), command = partial(Pressed,'PI'))
   pi_button.grid(row = 2, column = 5)

   # euler's number button
   e_button = Button(b_frame, text = 'e', fg = 'blue', width = dbw, height = dbh, font = (None, 14), command = partial(Pressed,'e'))
   e_button.grid(row = 3, column = 5)
      
   
def Place_Label():

   global calc_line
   calc_line = Label(calc, bg = 'white', relief = SUNKEN, width = 32, height = 1, text = '', font = (None, 16), bd = 5, anchor = 'w')
   calc_line.pack(side = TOP)   


def Calculator():
   Place_Label()
   Place_Buttons()
   calc.mainloop()
   
   
def Main():
   Calculator()


if __name__ == '__main__':
   Main()
   
