'''
Welcome to bill watch:
Get to know what is being passed and who is passing it.

Give it to me straight
1) Short quiz (affiliation and top issues) and see top bills that you think are related to it
    - Pay for a summary to show up as a newletter in you inbox

Full Control
1) Place a watch on certain filters i.e a certain congress person, bills passed in both houses
    - Pay for an API

'''

from Functions.control import filters
from Functions.give import quiz

def main():
    Menu_Input = input(
    """
    Hi There!\n
    So I hear you want to stay informed on politics... \n
    I am really proud of ya and so would the founding fathers \n
    (Unless you are a women, POC, indeginous, etc 😃 ) \n
    Do you want something curated based on your interests or full control 🧐🤨 \n
    Menu:\n
    1) Give it to me straight\n
    2) I want full control\n
    3) Quit\n

    Put your input here: 
    """).strip().lower()
    
    if Menu_Input == 1:
        filters()
    elif Menu_Input == 2:
        quiz()
    else:
        exit()

main()