import random, time, keyboard
from termcolor import colored
import pyautogui as key
import os
import threading

os.system("cls") # if ur on a mac or linux sucks 2 be u

prefixes = ['calc', 'process', 'compute', 'eval', 'gen', 'transform', 'create']
suffixes = ['Data', 'Result', 'Value', 'Output', 'Sum', 'Product', 'Equation']

WEIGHT_BETWEEN_BLOCKS = 4

math_expressions = [
    'a + b',
    'x * y',
    'z / 2',
    'math.sqrt(a)',
    'math.sin(b)',
    'math.cos(a + b)',
    'math.tan(x * y)',
]

def generate_lua_code():
    function_name = random.choice(prefixes) + random.choice(suffixes)
    math_line = random.choice(math_expressions)
    
    # Generate the Lua code
    lua_code = f"""
function {function_name}(a,b,c,x,y,z)
local result = {math_line}
return(result)
"""
    return lua_code

print(colored("[?]", "yellow"), "Press 5 to start generating code")

def type_random_block():
    gibberish_code = generate_lua_code()

    for char in gibberish_code:
        key.write(char)
        time.sleep(0.01)
        #if char == '\n':
        #    time.sleep(0.1)
            #pyautogui.press('enter')

    # down arrow twice to get to the end of the code
    key.press('down')
    time.sleep(0.1)
    key.press('down')
    time.sleep(0.1)

    key.press('enter')
    key.press('enter')



generating = False
t = None
while True:
    if keyboard.is_pressed('5'):
        generating = not generating 
        time.sleep(0.5)
        if generating:
            print(colored("[!]", "green"), "Generating code")
            t = threading.Thread(target=type_random_block)
            t.start()
        else:
            print(colored("[!]", "red"), "Stopped generating code")
            # stop the thread
            t.join()
