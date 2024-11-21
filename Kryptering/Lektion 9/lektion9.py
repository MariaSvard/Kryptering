## Läsa in filer

# with open('langsiktighet.jpg', "rb") as file: # läser in filen i binär data
#     data = file.read() # läser in filen(binärt) i variabeln data

# with open("horses.jpg", "wb") as new_file:
#     new_file.write(data)

# ledtrådar att göra projektet
# läsa in vilken fil som helst, kryptera
# hela filen i en variabel

## argparse ##

import argparse

parser = argparse.ArgumentParser(description="Exempelverktyg") # Beskrivning av verktyget, i projektet

# parser.add_argument("name", help="Här anger du ditt namn") # argument att kunna skriva in i terminalen
# vad är det de vill att användaren ska skicka in?
# "name" är då ett måste och behöver anges av användaren.

# parser.add_argument("age", type=int, help="Ange din ålder här")

# sätter man en flagga innan -- så är det frivilligt för användaren
# parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info") # mer information
# action=store_true kontrollerar om den finns med

# args = parser.parse_args() # hämtar alla argument som man har

# if args.verbose: # kontrollerar om användaren lagt till verbose
#     print(f"Hej {args.name}. Du är {args.age}")
# else:
#     print(f"Hej {args.name}")

## Detta skulle räcka till projektet ##

# parser.add_argument("name", help="Här anger du ditt namn") # argument att kunna skriva in i terminalen
# vad är det de vill att användaren ska skicka in?
# "name" är då ett måste och behöver anges av användaren.

# parser.add_argument("age", type=int, help="Ange din ålder här")

# sätter man en flagga innan -- så är det frivilligt för användaren
# parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info") # mer information
# action=store_true kontrollerar om den finns med
# parser.add_argument("-c", "--city", help="Ange din stad", default="Okänd stad")
# default = vad som kommer hända om användaren inte anger detta(ha ett värde som finns där tills man anger något annat)
# parser.add_argument("-m", "--mode", choices=["enkel", "detaljerad"], help="Välj läge") # coices tar en lista med []

# args = parser.parse_args() # hämtar alla argument som man har

# if args.mode == "detaljerad": # kontrollerar om användaren lagt till verbose
#    print(f"Hej {args.name}. Du är {args.age}. Du bor i {args.city}")
# else:
#    print(f"Hej {args.name}")