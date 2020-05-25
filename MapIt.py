# This program will open a Google Maps page with a given address.

import webbrowser, sys, pyperclip

# Command line arguments are stored in a list in the sys.argv variable.
sys.argv # ['MapIt.py', 'house number', 'street name', 'street']

# Check if command line arguments were passed.
# Else, use text from the clipboard.
if len(sys.argv) > 1:
     # ['MapIt.py', 'house number', 'street name', 'street'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
    
else: 
    address = pyperclip.paste()
    
# Open a Google Maps page with the input address.
# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
