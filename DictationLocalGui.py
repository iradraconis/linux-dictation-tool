#!/usr/bin/python3

# v0.7 Stand: 11.12.2021
# --------------------------------------------------------------------------------------------------------------
# Use: die Aufnahme wird durch den Sprachbefehl "exit" beendet
# Skript auf einen Hotkey legen: in Gnome ein Tastaturkürzel hinzufügen und den Befehl
# /home/DEINNAME/SKRIPTSPEICHERORT/Diktieren.sh; dann Shell-Skript erstellen, welches dann das Python-Skript
# startet. 
# Bsp. Skript
# #!/usr/bin/env bash
# python3 /home/max/Skripte/DictationLocalGui.py
# bash
#
# Installation: (hier Fedora Linux, ansonsten den distroeigenen Paketmanager benutzen):
# pip installieren, das vereinfacht das Installieren von Packages und Modulen
# sudo dnf install python3-pip
#
# XDOTool installieren mit 
# sudo dnf install xdotool
#
# TKinter installieren für GUI
# sudo dnf install python-tk
#
# Developer Tools installieren, damit pyaudio installiert werden kann
# sudo dnf groupinstall "Development Tools" "Development Libraries"
# 
# sudo dnf install portaudio-devel
# pip install pyaudio
# pip install SpeechRecognition
# --------------------------------------------------------------------------------------------------------------

import speech_recognition as sr
import subprocess # für den Aufruf von XDOTool (nur unter X11, ansonsten Ydotool unter Wayland)
import time
import tkinter
from tkinter import scrolledtext 
import sys

# Funktion für die Schaltfläche Ende
def ende():
    main.destroy()

# Funktion für das eigentliche Diktieren
def dictate():
    while True:
        try:
            with sr.Microphone() as source:
                listener = sr.Recognizer()
                #print('...')
                voice = listener.listen(source)
                #sr.adjust_for_ambient_noise(mic, duration=0.2)
                text = listener.recognize_google(voice, language="de-DE")
                #print(text) # gibt den Text im Terminal aus, wenn Skript mit Terminal gestartet wird
                if text == 'exit': # funktioniert nur mit Sprechpause
                    break
                subprocess.call(["xdotool", "type", text, " "]) # Leerzeichen => neuer Satz beginnt in LibreOffice mit Großbuchstaben
                #text_area.insert('end', text)                
        except:
            pass

# Hauptfenster
main = tkinter.Tk()
main.title(string='')

#Creating scrolled text area widget
'''text_area = tkinter.scrolledtext.ScrolledText(main, 
                                      wrap = tkinter.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Arial",
                                              15))
  
text_area.focus() # Placing cursor in the text area
text_area.pack()'''

# Schaltfläche Diktat starten
bstart = tkinter.Button(main, width = 3, height = 2, text = "REC", command = dictate)
bstart["font"] = "Arial 22 bold"
bstart.pack()

# Schaltfläche Ende
bende = tkinter.Button(main, width = 6, text = "Ende", command = ende)
bende.pack()

#Make the window jump above all
main.attributes('-topmost',True)

# Endlosschleife für das Hauptfenster
main.mainloop()
