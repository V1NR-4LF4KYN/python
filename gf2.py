import random;

# Variablen
i = random.randint(6, 110); # Die Startzahl i
print(f'Startzahl: {i}');

# Zwischenspeicher zum Berechnen, ob + oder - nötig ist.
temp = 0;
anfangszahl = i;

# Starte damit einmal + zu rechnen
temp = i + 1;

while i != 5:
    # Abfragen ob temp näher oder weiter von 5 entfernt ist als die Startzahl i
    if (temp - 5) > (i - 5):
        i -= 1;
        print(i)
    else:
        i += 1
        print(i)