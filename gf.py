'''
Hallo lieber Fragesteller,


ich habe deinen Code etwas überarbeitet:


Du hast zwei If-Abfragen gemacht, und das ist tatsächlich etwas ineffizient.
Das Problem dabei ist nämlich, dass beide if-Abfragen abgefragt werden, obwohl
ja eigentlich nur eine laufen müsste, weil wenn man weiß, dass man KM umwandeln möchte, dann
braucht man nichtmehr überprüfen, ob man Meilen umwandeln möchte.


    --> Dabei hilft elif, bzw. "else if" ;)






Du brauchst keine zwei Variablen für die Message und für das Result.
    --> Du kannst sie ja einfach überschreiben, je nachdem wofür du sie brauchst.


-------------------
Erklärung f-Strings:
Funktioniert ganz einfach
-> Hier ein Beispiel für einen normalen leeren String: ''
-> Hier ein leerer f-string: f''


Jetzt kannst du, wie ich es gemacht habe noch {} ergänzen und
überall dort wo du Variablen stehen haben möchtest schreibst
du diese in geschweifte Klammern.
Beipiel: f'Hallo ich bin ein Beipiel und hier folgt eine Variable: {var}.


Danke fürs Lesen!


PS - Ich hoffe das hilft dir in Zukunft :D


'''


# Variablen:
schreibweisenKM = ['meilen', 'miles', 'mi']
schreibweisenMI = ['kilometer', 'km']


# Input/Abfrage des Users
kmormi = input("Möchtest du Meilen oder Kilometer umrechnen? Mi oder Km?\n\n").lower() # wandelt den Input in Kleinbuchstaben um 




# Dadurch, dass nur noch Kleinbuchstaben im Input sind kann man die Bedingung erheblich kürzen.
# Zudem kannst du abfragen, ob kmormi in der Liste schreibweisenKM ist und das war es ^^
if kmormi in schreibweisenKM:    
    message = input("Bitte die Anzahl der Meilen eingeben!\n\n") 


    result = float(message) * 1.60934 


    print(f'{message} Meilen sind {result} Kilometer') # Hier benutze ich einen "f-string". Erklärt habe ich ihn oben.




elif kmormi in schreibweisenMI: # Falls Meilen umgewandelt werden sollen


    message = float(input("Bitte die Anzahl der Kilometer eingeben!\n\n"))


    result = float(message) * 0,621371


    print(f'{message} Kilometer sind {result} Meilen') # Noch ein "f-string" ;)




else: # Für den Fall, dass der Input falsch war
    print('Falscher Input. Beende...')






''' Ich hoffe ich konnte helfen! '''
# Schreibe Fragen in die Kommentare oder auch privat.