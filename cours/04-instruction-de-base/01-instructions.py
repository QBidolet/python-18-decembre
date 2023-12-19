nombre_1 = 25
nombre_2 = 50

# condition
if nombre_1 > nombre_2:
    print("Nombre_1 est plus grand.")
elif nombre_1 == nombre_2:
    print("Nombre1 et nombre2 sont égaux.")
else:
    print("Nombre 2 est supérieur à nombre 1.")

# boucle while
i = 0
while i < 6:
    print(i)
    i += 1

print("#" * 25)
# for avec range
# for(int i=0; i<5; i++)
# range(end)
for i in range(6):
    print(i)

print("#" * 25)
# range(start, end, step)
for i in range(3, 30, 3):
    print(i)

print("#" * 25)
# break et continue
i = 0
while i < 6:
    if i == 2:
        # break
        i += 1
        continue
    print(i)
    i += 1