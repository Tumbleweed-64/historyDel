import os
osType = input("Before we start, what OS are you using? (macos, windows, linux")
userName = ""
historyPath = ""
if osType.lower() == "windows":
    userName = input("What's your username? (used for concatenating in filepath) ")
    historyPath = "C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    os.remove(historyPath)
    print("History deleted. Tool made by Tumbleweed-64 on GitHub.")
elif osType.lower() == "macos":
    userName = input("What's your username? (used for concatenating in filepath) ")
    historyPath = "/Users/" + userName + "/Library/Application Support/Google/Chrome/Default"
    os.remove(historyPath)
    print("History deleted. Tool made by Tumbleweed-64 on GitHub.")
elif osType.lower() == "linux":
    userName = input("What's your username? (used for concatenating in filepath) ")
    historyPath = "/home/" + userName + "/.config/google-chrome/Default"
    os.remove(historyPath)
    print("History deleted. Tool made by Tumbleweed-64 on GitHub.")
