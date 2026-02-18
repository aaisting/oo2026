numbrid=[int(nr) for nr in "3760503029"]
koefd=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(list(zip(numbrid, koefd)))
print([paar[0]*paar[1] for paar in zip(numbrid, koefd)])
print(sum([paar[0]*paar[1] for paar in zip(numbrid, koefd)]))
print(sum([paar[0]*paar[1] for paar in zip(numbrid, koefd)]) % 11)