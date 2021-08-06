#!/usr/bin/python3

# v0.6 Stand: 03-08-2021

# Installation:
# XDOTool installieren mit 
# sudo dnf install xdotool
#
# Developer Tools installieren, damit pyaudio installiert werden kann
# sudo dnf groupinstall "Development Tools" "Development Libraries"
# sudo dnf install portaudio-devel
# pip install pyaudio
# pip install speech_recognition

# --------------------------------------------------------------------------------------------------------------
# Use: die Aufnahme wird durch den Sprachbefehl "exit" beendet
# Skript auf einen Hotkey legen: in Gnome ein Tastaturkürzel hinzufügen und den Befehl
# /home/DEINNAME/SKRIPTSPEICHERORT/Diktieren.sh; dann Shell-Skript erstellen, welches dann das Python-Skript
# startet. 
# Bsp. Skript
# #!/usr/bin/env bash
# python3 /home/USERNAME/Skripte/DictationLocalGui.py
# bash
#
# Installation (hier Fedora Linux, ansonsten den distroeigenen Paketmanager entsprechend benutzen):
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
# pip install speech_recognition
# --------------------------------------------------------------------------------------------------------------

import speech_recognition as sr
import subprocess
import time
import tkinter
import sys

# Funktion Schaltfläche Ende
def ende():
    main.destroy()

# Funktion Diktieren
def dictate():
    while True:
        try:
            with sr.Microphone() as source:
                listener = sr.Recognizer()
                print('...')
                voice = listener.listen(source)
                text = listener.recognize_google(voice, language="de-DE")
                print(text) # gibt den Text zusätzlich im Terminal aus, wenn Skript mit Terminal gestartet wird
                if text == 'exit': # Ende des Diktats - Sprechpause!
                    break
                subprocess.call(["xdotool", "type", text, " "]) # Leerzeichen => neuer Satz beginnt in LibreOffice mit Großbuchstaben                             
        except:
            pass

# Hauptfenster
main = tkinter.Tk()
main.title(string='Diktieren mit der Google API')

# Schaltfläche Diktat starten
bstart = tkinter.Button(main, width = 15, height = 3, text = "Diktat starten", command = dictate)
bstart["font"] = "Arial 34 bold"
bstart.pack()

# Label Hinweis zum Beenden des Diktats
tlabel = tkinter.Label(main, text = "-- sag 'Exit' zum Beenden des Diktats --")
tlabel["font"] = "Arial 9"
tlabel.pack()

# Schaltfläche Ende
bende = tkinter.Button(main, text = "Ende", command = ende)
bende.pack()

# Endlosschleife für das Hauptfenster
main.mainloop()
