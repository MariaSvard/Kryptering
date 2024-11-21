import argparse # standardbibliotek, behöver inte göra pip install #
# man kan också importera egna filer, så man kan aldrig kalla filerna för samma sak som man importerar(bibliotek)

parser = argparse.ArgumentParser(description="Mitt krypteringsverktyg") # ge en förklaring vad verktyget gör
# skapa en variabel

## ovan är hur man startar sitt argparse argument ##

parser.add_argument("name", help="Ange ditt namn") # vad du vill kalla det, 
parser.add_argument("age", type=int, help="Ange din ålder") 
# help gör det lättare för användaren att veta vad som ska anges, # kommer upp när användaren behöver hjälp --help
# ovan kommer kräva att användaren anger argumenten

parser.add_argument("-v", "--verbose", action="store_true", help="Visa mer information")
# - eller -- ger flaggor, används för att lägga till alternativ
# när man lägger till flaggor så kommer krävs det inte av användaren att ange argument 
# --verbose, standardsätt för att göra något, -v för att skriva ut mer information, de gör samma sak
# action=store_true för att se om den är tillagd eller inte, är flaggan tillagd av användaren

args = parser.parse_args() # hur man fångar upp vad användaren skriver in

if args.verbose: # om användaren angett flaggan, vad ska göras?
    print(f"Hej {args.name}, din ålder: {args.age}")
else:
    print(f"Hej {args.name}")

print(f"Hej {args.name}")

