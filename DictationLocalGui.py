#!/usr/bin/python3

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# v0.6 Stand: 03-08-2021

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
