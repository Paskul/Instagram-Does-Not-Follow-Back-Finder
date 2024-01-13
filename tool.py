import PySimpleGUI as sg
import json

def getList(folder_path):
    try:
        followersFile = folder_path + "/connections/followers_and_following/followers_1.json"
        followingFile = folder_path + "/connections/followers_and_following/following.json"

        f1 = open(followersFile)
        f2 = open(followingFile)

        followers = json.load(f1)
        following = json.load(f2)

        users = []

        for user in following['relationships_following']:
            id = user['string_list_data'][0]['value']
            users.append(id)

        for user in followers:
            id = user['string_list_data'][0]['value']
            if id in users:
                users.remove(id)
            
        for person in users:
            print(person)

        return users
    
    except FileNotFoundError:
        return "FALSE"

# Define the layout
layout = [
    [sg.Text("Select Folder:"), sg.Input(key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Button("Run"), sg.Button("Exit")],
    [sg.Multiline(size=(60, 20), key='-OUTPUT-', autoscroll=True)]
]

# Create the Window
window = sg.Window("Does Not Follow Back Tool", layout)

# Event Loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "Run":
        folder_path = values['-FOLDER-']
        if folder_path:
            output = getList(folder_path)
            formatted_output = "Incorrect Downloaded File! Try again!\nPotentially move back a few files, or unzip for the folder.\nShould look something like...\nC:/Users/name/Desktop/instagram-username-2024-01-01-xyz123"
            if output != "FALSE":
                formatted_output = '\n'.join(output)  # Join list items into a single string with newlines
            window['-OUTPUT-'].update(formatted_output)
        else:
            sg.popup("Please select a folder first!")

window.close()