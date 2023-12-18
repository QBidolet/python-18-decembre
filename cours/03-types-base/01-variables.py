# Les noms de variables utilisent snake_case
# TOUT alphabet sauf les caractères spéciaux comme @ ! , ? ...
# Un nom de variable ne doit pas commencer par un chiffre ou un underscore.

ma_boite = 42
ma_boite_2 = ma_boite
print(ma_boite)
print(ma_boite_2)
ma_boite = 45.5
print(id(ma_boite), id(ma_boite_2), id(42))

# noms de variables valides
# a
# a1
# a_b_c
# _a
# un_mot

# noms de variables invalides
# 1a
# a!

