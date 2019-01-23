import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")


inputText = input("Please enter the text or pharase : " , )
speak.Speak(inputText)
