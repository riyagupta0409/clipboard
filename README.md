# Project Name
CLIPBOARD PROJECT

-------------
ABOUT PROJECT
-------------
This project works similar to the clipboard and copy-paste operations present in our system with additional features like editing 
After running backend script in the background you can copy items and it will be automatically added in your personal clipboard 
On opening clipboard user has several features like paste  (mentioned below) 

-------------
DEPENDENCIES
-------------
Modules:
	1. os
	2. datetime
	3. pyperclip
	4. sqlite3
	5. pyautogui  --> for windows 
	6. readline --> for unix 

Running Files:
	1. To run copy operations script run --> pythonw backend_copy_script.py
	2. To work on the clipboard run -->  python clipboard_main.py

Files :
	1. backend_copy_script --> to operate the copy operations . It will wait for the user to copy some text and once copied
							   will be added to your clipboard . 
	2. clipboard_database --> handling all methods and interactions with the database 
	3. clipbaord_main --> handling user request and giving response (Interface between database and ui )
	4. clipboard_ui --> includes the part which is shown on the user's screen 


--------
FEATURES 
--------
1. copy --> by running the backend_script user can copy elements to the clipboard
2. paste --> user can select text from the clipboard and can paste it anywhere
3. add new text --> user can manually add text to the clipboard
4. remove manually--> you can manually remove a text from clipboard
5. remove automatically --> text would be removed automatically after 2 days 
6. pin items --> items can be pinned so that it doesn't get removed automatically
7. unpin items ---> unpin the pinned items and reset it's priority 


-------
SOURCES
------- 
1. https://pyperclip.readthedocs.io/


----------
CODE FILES
----------
https://github.com/riyagupta0409/clipboard
