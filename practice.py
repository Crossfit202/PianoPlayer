from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import os
import time

#example of wav - AudioSegment.from_file("piano-88-notes/4-ds.wav")


def main():
    
    userInput = 0

    while userInput != 6:
        clear_console()
        menu()
        userInput = get_input()
        global song
    
        if userInput == 1: # Play a note

            clear_console()
            print("You can play a sharp by entering s. Ex - cs")
            noteInput = input("What note would you like to play? (c/d/e/f/g/a/b): ")
            octaveInput = int((input("What octave would you like? (1-8): ")))
            play_note(noteInput, octaveInput)
        
        elif userInput == 2: #Play a chord

            clear_console()
            majorOrMinor = input("Would you like to play a major or a minor chord? (M/m): ")
            chordInput = input("What is the base note of the chord? (c/d/e/f/g/a/b): ")
            octaveInput = int(input("Which octave would you like? (1-8): "))

            play_chord(chordInput, octaveInput, majorOrMinor)

        elif userInput == 3: #Make a song
            clear_console()
            print("In this mode, you will write out what you would like to play seperated by commas.")
            print("To call a single note, simply type the note. Ex - c")
            print("To make it a sharp, put an s afterwards. Ex - cs")
            print("To specify the octave, put the number representing the octave before the note. Ex - 4c")
            print("To call a chord, put an asterisk afterwards. Ex- 4c*")
            print("To call a major or minor chord, put either a capital M (for major) or lower case m (for minor) at the end. Ex - 4c*M")
            
            print("Put it all together and you should end up with a song that looks something like this:")
            print("4c, 4d, 4c*M, 4e, 4f*M, 4g*M, 4a*M, 4b*M, 5c*M")
            print("")
            print("\nYou can now make your own song! Press enter when you're finished")

            
            song = input("")
            play_song(song)

        elif userInput == 4: #Play a song from a file
            fileName = input("Which song would you like to open? Ex - mysong: ")
            play_from_file(fileName)

        elif userInput == 5: #Save a song to a file
            fileName = input("What would you like to name the file? Ex - mysong: ")
            save_string_as_file(song, fileName)


def save_string_as_file(string_to_save, file_name):
    # Prompt the user to enter a file name


    # Open the file for writing
    with open(file_name, "w") as output_file:
        # Split the string at the commas
        string_parts = string_to_save.split(",")
        # Write each string part to a new line in the file
        
        for part in string_parts:
            output_file.write(part.strip() + "\n")
    

def play_song(song):
    reply = input("Would you like to play your song? (y/n): ")

    if reply.lower() == "y":
        fileName = "playfile"
        save_string_as_file(song, fileName)
        play_from_file(fileName)

def play_from_file(file):
    
    #octaveList = []
    #noteList = []
    #chordList = []
    #majorMinorList = []
    with open(file, 'r') as song:
        #data = f.read()
        for line in song: 
            if "*" in line.rstrip():
                if len(line.rstrip()) == 4:
                    #octaveList.append(line.rstrip()[0])
                    #noteList.append(line.rstrip()[1])
                    #chordList.append("T")
                    #majorMinorList.append(line.rstrip()[3])

                    octave = (line.rstrip()[0])
                    note = (line.rstrip()[1])
                    majorMinor = (line.rstrip()[3])

                    play_chord(note, octave, majorMinor)
                
                if len(line.rstrip()) == 5:
                    #octaveList.append(line.rstrip()[0])
                    #noteList.append(line.rstrip()[1] + line.rstrip()[2])
                    #chordList.append("T")
                    #majorMinorList.append(line.rstrip()[4])
                    
                    octave = (line.rstrip()[0])
                    note = (line.rstrip()[1] + line.rstrip()[2])
                    majorMinor = (line.rstrip()[4])

                    play_chord(note, octave, majorMinor)
                    
            else:
                if len(line.rstrip()) == 2:
                    #octaveList.append(line.rstrip()[0])
                    #noteList.append(line.rstrip()[1])
                    #chordList.append("F")
                    #majorMinorList.append("F")

                    octave = (line.rstrip()[0])
                    note = (line.rstrip()[1])
                    
                    play_note(note, octave)

                if len(line.rstrip()) == 3:
                    #octaveList.append(line.rstrip()[0])
                    #noteList.append(line.rstrip()[1] + line.rstrip()[2])
                    #chordList.append("F")
                    #majorMinorList.append("F")

                    octave = (line.rstrip()[0])
                    note = (line.rstrip()[1] + line.rstrip()[2])
                    
                    play_note(note, octave)   
        
    input("")

def menu():
    print("Welcome to the piano player!")
    print(" 1. Play a note \n 2. Play a chord \n 3. Make a song \n 4. Play a song from a file \n 5. Save a song to a file \n 6. Quit")
    

def get_input():
    userInput = input("Please select an option from the menu: ")
    return int(userInput)

def note_string(note, octave):
    noteString = (f"piano-88-notes/{octave}-{note}.wav")
    return noteString

def play_note(note, octave):
    duration = 2000
    sound = AudioSegment.from_file(note_string(note, octave))
    sound = sound[:duration]

    play(sound.fade_out(200))

def play_chord(note, octave, majorOrMinor):

    #Major Chords
    if majorOrMinor == "M":
        if note.lower() == "c":
            note1 = note_string(note, octave)
            note2 = note_string("e", octave)
            note3 = note_string("g", octave)

        elif note.lower() == "cs":
            note1 = note_string(note, octave)
            note2 = note_string("f", octave)
            note3 = note_string("gs", octave)

        elif note.lower() == "d":
            note1 = note_string(note, octave)
            note2 = note_string("fs", octave)
            note3 = note_string("a", octave)

        elif note.lower() == "ds":
            note1 = note_string(note, octave)
            note2 = note_string("g", octave)
            note3 = note_string("as", octave)

        elif note.lower() == "e":
            note1 = note_string(note, octave)
            note2 = note_string("gs", octave)
            note3 = note_string("b", octave)

        elif note.lower() == "f":
            note1 = note_string(note, octave)
            note2 = note_string("a", octave)
            note3 = note_string("c", octave)

        elif note.lower() == "fs":
            note1 = note_string(note, octave)
            note2 = note_string("as", octave)
            note3 = note_string("cs", octave + 1)

        elif note.lower() == "g":
            note1 = note_string(note, octave)
            note2 = note_string("b", octave)
            note3 = note_string("d", octave)

        elif note.lower() == "gs":
            note1 = note_string(note, octave)
            note2 = note_string("c", octave + 1)
            note3 = note_string("ds", octave + 1)

        elif note.lower() == "a":
            note1 = note_string(note, octave)
            note2 = note_string("cs", octave)
            note3 = note_string("e", octave)

        elif note.lower() == "as":
            note1 = note_string(note, octave)
            note2 = note_string("d", octave + 1)
            note3 = note_string("f", octave + 1)

        elif note.lower() == "b":
            note1 = note_string(note, octave)
            note2 = note_string("ds", octave)
            note3 = note_string("fs", octave)

    #Minor Chords
    elif majorOrMinor == "m":
        if note.lower() == "c":
            note1 = note_string(note, octave)
            note2 = note_string("ds", octave)
            note3 = note_string("g", octave)

        elif note.lower() == "cs":
            note1 = note_string(note, octave)
            note2 = note_string("e", octave)
            note3 = note_string("gs", octave)

        elif note.lower() == "d":
            note1 = note_string(note, octave)
            note2 = note_string("f", octave)
            note3 = note_string("a", octave)

        elif note.lower() == "ds":
            note1 = note_string(note, octave)
            note2 = note_string("fs", octave)
            note3 = note_string("as", octave)

        elif note.lower() == "e":
            note1 = note_string(note, octave)
            note2 = note_string("g", octave)
            note3 = note_string("b", octave)

        elif note.lower() == "f":
            note1 = note_string(note, octave)
            note2 = note_string("gs", octave)
            note3 = note_string("c", octave)

        elif note.lower() == "fs":
            note1 = note_string(note, octave)
            note2 = note_string("a", octave)
            note3 = note_string("cs", octave + 1)

        elif note.lower() == "g":
            note1 = note_string(note, octave)
            note2 = note_string("as", octave)
            note3 = note_string("d", octave)

        elif note.lower() == "gs":
            note1 = note_string(note, octave)
            note2 = note_string("b", octave + 1)
            note3 = note_string("ds", octave + 1)

        elif note.lower() == "a":
            note1 = note_string(note, octave)
            note2 = note_string("c", octave)
            note3 = note_string("e", octave)

        elif note.lower() == "as":
            note1 = note_string(note, octave)
            note2 = note_string("cs", octave + 1)
            note3 = note_string("f", octave + 1)

        elif note.lower() == "b":
            note1 = note_string(note, octave)
            note2 = note_string("c", octave)
            note3 = note_string("fs", octave)


    sound1 = AudioSegment.from_file(note1)
    sound2 = AudioSegment.from_file(note2)
    sound3 = AudioSegment.from_file(note3)

    duration = 2000
    sound1 = sound1[:duration]
    sound2 = sound2[:duration]
    sound3 = sound3[:duration]

    overlayed_sound = sound1.overlay(sound2).overlay(sound3)

    play(overlayed_sound.fade_out(200))

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/Mac
    else:
        os.system('clear')

main()

