import random
import string

length = int(input('\nLänge des Passwortes: '))

all = string.ascii_letters + string.digits + string.punctuation
print("".join(random.sample(all,length)))

