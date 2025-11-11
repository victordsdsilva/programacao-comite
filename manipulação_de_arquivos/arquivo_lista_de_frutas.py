frutas = ['uva', 'laranja', 'banana', 'pera']

with open("frutas.txt", "w") as f:
    for n in frutas:
        f.write(n + "\n")