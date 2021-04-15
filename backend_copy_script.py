# # import all necessary modules 
import sqlite3 as sq
from datetime import datetime , date , time
from os import system
import pyperclip as pc 
import time 

# # import our modules
import clipboard_database as cd
new_clipboard_item = cd.database()
new_clipboard_item.make_clipboard_table()


# # infinite loop to run in background 
# # checks if a new element has been added to clipboard
# # it will be added to our database as well 
pc.paste()
while True:
	x = pc.waitForNewPaste()
	text = pc.paste()
	print(text )
	new_clipboard_item.add_new_item(text )
	time.sleep(2)


	
