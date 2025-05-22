# In your keyboard press windows + r
# Now write cmd
# If you have VS or an application for programming, copy the code, if not, download VS in visualstudio download
# copy the code and go to the chat
# click start in the top with the icon " > "

import pyautogui # Import pyautogui
import time # Import a time for write

count = 0 # The count is 0
name = "Kharla" # Set a name for your girlfriend or your boyfriend or your friend

time.sleep(10) # 10 seconds for write (count) - I love you so much (name)
while True:
    count += 1 # Sum the count with the number 1
    pyautogui.write(f'{count} - I love you so much {name}') # IMPORTANT -- Write message
    pyautogui.press('enter') # IMPORTANT -- The bot has been pressed in your keyboard the key enter
    if count == 100: # If count is 100
        break # The loop is finish
