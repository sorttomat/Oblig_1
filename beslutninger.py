# Dette programmet spoer brukeren om hen har lyst paa en brus. Svaret til brukeren avgjor hva som skjer videre.

answer = input("Kunne du tenke deg en brus? (ja/nei) ") # Programmet ber brukeren om en input. Svaret blir lagret i en variabel.

if answer == "ja": # Hvis brukeren skrev inn akkurat "ja", utforer programmet linjen under. Ellers hopper det videre.
    print("Her har du en brus!")
elif answer == "nei": # Hvis svaret var akkurat "nei", utforer programmet linjen under. Ellers hopper det videre.
    print("Den er grei.")
else: # I alle andre tilfeller enn de beskrevet over, utforer programmet linjen under denne. 
    print("Det forsto jeg ikke helt.")

