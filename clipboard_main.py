# importing database and ui files 
import clipboard_ui as c_ui
import clipboard_database as cd

# importing other modules
import time
import sys


# fatures class acting as an interface 
# listening to user's request fetching data from 
class feature :

	def main_screen(self):

		rows = clipboard_database_object.database_clipboard_rows() # fetching clipboard rows
		clipboard_ui_object.display_main_screen(rows) # showing main screen

		# # asking task from user 
		print(" "*19,end="")
		choice = input("Enter a valid choice :- ")

		# # Assigning task according to the user's choice
		self.assign_task(choice)

	# # assign task according to the user choice
	def assign_task(self , choice):
		if choice == '1' :
			self.add_text_manually_feature()
		elif choice == '2' :
			self.remove_text_manually_feature()
		elif choice=='3':
			self.pin_text_feature()
		elif choice== '4':
			self.unpin_text_feature()
		elif choice== '5' :
			self.select_text_to_copy_feature()
		elif choice == '6':
			self.edit_text_feature()
		elif choice == '7':
			self.exit()
		else:
			clipboard_ui_object.display_error_message("Enter a valid choice !!")
			time.sleep(1)
		self.main_screen()



	# feature of adding text manually 
	def add_text_manually_feature(self ):

		# show the heading remove everything else
		clipboard_ui_object.display_clipboard_heading()

		# ask for text string 
		print(" "*19,end="")
		text = input("Enter Your text string :- ")

		# add text in db
		clipboard_database_object.add_new_item(text)

		# show successfully added message
		clipboard_ui_object.display_success_message('successfully added text to clipboard')
		time.sleep(1)

	# feature for removing text manually from clipboard
	def remove_text_manually_feature(self):

		# ask for text id 
		print(" "*19 , end="")
		text_id = input("Enter the text id associated with text you want to remove :- ")

		# remove task from db
		returned_value = clipboard_database_object.remove_selected_item(text_id)

		# checking returned value 
		if returned_value == 0: # invalid id 
			clipboard_ui_object.display_error_message('Entered id is not valid  !!')
		else: # successfully removed
			clipboard_ui_object.display_success_message('successfully removed Text from clipboard')
		time.sleep(1)

	# # Pin text feature 
	def pin_text_feature(self):

		# ask for text id 
		print(" "*19 , end="")
		text_id = input("Enter text id associated with text you want to pin :- ")

		# pin item in db
		returned_value = clipboard_database_object.pin_item(text_id)

		# checking returned value 
		if returned_value == 0: # invalid id 
			clipboard_ui_object.display_error_message('Entered id is not valid  !!')
		else: # successfully removed
			clipboard_ui_object.display_success_message('successfully Pinned Text to clipboard')
		time.sleep(1)

	# unpin a text
	def unpin_text_feature(self):

		# ask for text id 
		print(" "*19 , end="")
		text_id = input("Enter text id associated with text you want to unpin :- ")

		# pin item in db
		returned_value = clipboard_database_object.unpin_item(text_id)

		# checking returned value 
		if returned_value == 0: # invalid id 
			clipboard_ui_object.display_error_message('Entered id is not valid  !!')
		else: # successfully removed
			clipboard_ui_object.display_success_message('successfully Pinned Text to clipboard')
		time.sleep(1)		


	# allows user to select a text to paste 
	def select_text_to_copy_feature(self):

		# ask for text id 
		print(" "*19 , end="")
		text_id = input("Enter text id associated with text you want to select :- ")

		# # copy from db 
		returned_value = clipboard_database_object.select_item_to_paste(text_id)

		# checking returned value 
		if returned_value == 0: # invalid id 
			clipboard_ui_object.display_error_message('Entered id is not valid  !!')
		else: # successfully removed
			clipboard_ui_object.display_success_message('successfully copied Text to clipboard')
			clipboard_ui_object.display_success_message('You can now use paste command or ctrl+v to paste it anywhere ')
		time.sleep(3)			

	# feature to update existing text
	def edit_text_feature(self):

		# ask for text id 
		print(" "*19 , end="")
		text_id = input("Enter text id associated with text you want to select :- ")

		# show the heading remove everything else
		clipboard_ui_object.display_clipboard_heading()

		# # copy from db 
		returned_value = clipboard_database_object.edit_item_text(text_id)

		# checking returned value 
		if returned_value == 0: # invalid id 
			clipboard_ui_object.display_error_message('Entered id is not valid  !!')
		else: # successfully removed
			clipboard_ui_object.display_success_message('successfully Edited text ')
		time.sleep(1)

	def exit(self):
		cd.conn.close() # closing database connection
		sys.exit() # exiting 


# main function to run project 
if __name__ == '__main__' :

	# make a clipboard database object to connect it to the database
	clipboard_database_object = cd.database()
	clipboard_database_object.make_clipboard_table() # make clipboard table if not exist
	clipboard_database_object.remove_outdated_items() # remove outdated elements from 

	# ui object to react with ui 
	clipboard_ui_object = c_ui.UI()

	# feature object 
	clipboard_feature_object = feature()
	clipboard_feature_object.main_screen()
