# # import all necessary modules 
# import sqlite3 as sq
from os import system , name
import time 

# # importing database , feature files
# import clipboard_database as cd
# import clipboard_main as c_main 

# # Adding color to text in cmd
system("color")
COLOR = {
	"Bold":"\033[1m",
	"Dim":"\033[2m",
	"Underlined":"\033[4m",
	"HEADER": "\033[95m",
	"BLUE": "\033[94m",
	"YELLOW":"\033[33m",
	"GREEN": "\033[92m",
	"RED": "\033[91m",
	"ENDC": "\033[0m",   # # color-off
	"PURPLE":"\033[0;35m",
	"CYAN": "\033[0;36m"
}

# # Function for clearing CMD 
def clear():
	if name == "nt":
		_=system('cls')
	else:
		_=system('clear')


# # class for ui of the project
class UI:

	# # show error messages in red
	def display_error_message(self , text):
		print(COLOR["RED"]," "*19,text,COLOR["ENDC"])

	# # show Success messages in Green
	def display_success_message(self , text):
		print(COLOR["GREEN"]," "*19,text,COLOR["ENDC"])

	# # display_informational_message_in_blue
	def display_informational_message(self , text):
		print(COLOR["BLUE"]," "*19,text,COLOR["ENDC"])		


	# clipboard heading
	def display_clipboard_heading(self):

		clear()
		print(COLOR["BLUE"])
		print("""                     _______________________________________""")
		print("""                    |                                       |""")
		print("""                    |        YOUR PERSONAL CLIPBOARD        |""")
		print("""                    |_______________________________________|""")
		print(COLOR["ENDC"])

	# for restructuring the text string
	def restructure_text(self , text):
		items = text.split('\n')

		if len(items)==1: # if only single line string 
			print("",items[0],COLOR["ENDC"])
			return

		print("",items[0]) # for multiline strings
		for item in range(1,len(items)):
			if item == len(items)-1:
				print(" "*29 , "|",items[item],COLOR["ENDC"])
				return
			print(" "*29 , "|",items[item])

	# to show clipboard items 
	def display_clipboard_items(self, rows):

		if rows == 0:
			self.display_error_message(text)
			return 0 # empty clipboard 

		# # instructions about clipboard
		self.display_error_message("* pinned text is shown in green colour")
		self.display_error_message("* Unpinned text will be removed in 2 days ")
		print()

		# show all clipboard items 
		print(COLOR["BLUE"]," "*18," TEXT ID ","|","      TEXT",COLOR["ENDC"])
		j=1
		for row in rows:
			print(" "*29 , "|")

			if row[3] == 0:
				print(COLOR["Bold"]," "*18,str(row[0]).center(9),"|",end="")
				self.restructure_text(row[1])

			elif row[3] == 1: # for pinned items green color
				print(COLOR["GREEN"]," "*18,str(row[0]).center(9),"|",end="")
				self.restructure_text(row[1])
			j+=1

		return 1

	def display_main_screen(self , rows):

		self.display_clipboard_heading()
		returned_value = self.display_clipboard_items( rows)

		# # show choices available to user
		print()
		self.display_informational_message("1. Add New Text To clipboard")
		self.display_informational_message("2. Remove A Text From Clipboard")
		self.display_informational_message("3. Pin A Text ")
		self.display_informational_message("4. Unpin A Text")
		self.display_informational_message("5. Select A Text To Copy")
		self.display_informational_message("6. Edit A Text")
		self.display_informational_message("7. Exit From clipboard")
		print()


