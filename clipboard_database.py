# # import all necessary modules 
import sqlite3 as sq
from datetime import datetime , date , time
import pyperclip as pc 
import time

# importing module to give default value in our input area
try:
	from pyautogui import typewrite # Windows 
	autogui = True
except (ImportError, KeyError): # Unix
	import readline
	autogui = False

# # creating sqlite Connection
conn = sq.connect("project.db")
cur = conn.cursor()

# # function to give default to value to input area


# # database class for all methods of project's database 
class database :

	def rlinput(self , prompt, prefill=''):

		if autogui: # if module is pyautogui for windows 
			print(prompt)
			typewrite(prefill)
			return input()
		else: # if module is readline for unix
			readline.set_startup_hook(lambda: readline.insert_text(prefill))
			try:
				return input(prompt)
			finally:
				readline.set_startup_hook()

	# to check if the id used is valid or not 
	def is_valid_id(self , id_ ):

		# try to convert it into integer
		try :
			id_ = int(id_)
		except:
			return 0

		# if given value is not integer 
		if type(id_) != int :
			print("Enter an integer Value ")
			return 0

		# to check if given id exists or not 
		check_query = '''SELECT * FROM clipboard WHERE id= {}'''.format(id_)

		cur.execute(check_query)
		row = cur.fetchall()

		# # if given id doesn't exist
		if row == []:
			print("Item id doesn't exist !! ")
			return 0 

		return 1


	# make table to store clipboard items if not exist 
	# includes id , copied-text and datetime at which it is added
	def make_clipboard_table(self):

		sql_items_table = """CREATE TABLE IF NOT EXISTS clipboard(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					item_text TEXT NOT NULL,
					date_added date ,
					is_pinned INTEGER);
					"""

		cur.execute(sql_items_table)
		conn.commit()


	# adds new text to the clipboard
	def add_new_item(self , text_to_be_added ):

		date_to_be_added = datetime.today() # current date 

		q="""INSERT INTO clipboard(item_text , date_added , is_pinned )
		VALUES(?,?,?)"""

		cur.execute(q,(text_to_be_added,date_to_be_added,0)) # executes insert query 
		conn.commit() # committing changes
 

	# Shows the clipboard (fetching data from sql table n showing)
	def database_clipboard_rows(self) :
		# select everything from the clipboard table 
		 show_query = ''' SELECT * from clipboard'''

		 cur.execute(show_query)
		 rows = cur.fetchall()
		 return rows


	# Remove chosen item (removing items according to user )
	def remove_selected_item(self , item_id_to_be_removed):

		if not self.is_valid_id(item_id_to_be_removed):
			return 0

		# remove it with given id
		remove_query ="""DELETE FROM clipboard 
						WHERE id = {}""".format(item_id_to_be_removed)

		cur.execute(remove_query)
		conn.commit()
		return 1


	# Remove outdated items which are in clipboard for 
	# more than 7 days 
	def remove_outdated_items(self):

		current = datetime.today()

		remove_query = ''' DELETE FROM clipboard WHERE
						  date_added <= date('now', '-2 day') and is_pinned = 0
						'''

		cur.execute(remove_query)
		conn.commit()
		return 1


	# # pin items so that it doesn't get deleted automatically 
	def pin_item(self , id_to_be_pinned):

		if not self.is_valid_id(id_to_be_pinned):
			return 0 

		pin_query = '''UPDATE clipboard SET is_pinned = 1 
					WHERE id = {}'''.format(id_to_be_pinned )

		cur.execute(pin_query)
		conn.commit()
		return 1


	# unpin items so that get auto-deleted after 7 days 
	def unpin_item(self , id_to_be_unpinned):

		if not self.is_valid_id(id_to_be_unpinned):
			return 0 

		pin_query = '''UPDATE clipboard SET is_pinned = 0 
					WHERE id = {}'''.format(id_to_be_unpinned)

		cur.execute(pin_query)
		conn.commit()
		return 1


	# returns the text of given id
	def text_of_given_id(self , id_):

		if not self.is_valid_id(id_):
			return 0 

		select_query = '''SELECT item_text FROM clipboard 
						WHERE id = {}'''.format(id_)

		cur.execute(select_query)
		row = cur.fetchall()

		return row[0][0]		

	# Select item to paste -- selected item gets copied to os clipboard and 
	# # can be used using paste command
	def select_item_to_paste(self, id_of_given_item):

		text = self.text_of_given_id(id_of_given_item)
		if  text == 0:
			return 0

		# text to be copied to clipboard 
		paste_text = text
		pc.copy(paste_text)
		return 1


	# # edit option if user wants to edit some text 
	def edit_item_text(self , item_id_to_edit):

		text = self.text_of_given_id(item_id_to_edit)  # get task from it's id 
		if  text == 0:
			return 0

		# to give default value to input area 
		edited_text = self.rlinput('Edit -- ' , text) 

		update_query = '''UPDATE clipboard SET item_text = ? WHERE 
						id = ? '''

		cur.execute(update_query , (edited_text , item_id_to_edit) )
		conn.commit()

		return 1


