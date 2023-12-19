# Sans utiliser de nombres ni d'opérateurs mathématiques autre que le "=",
# échanger les valeurs de a et b.
# a = 6
# b = 5

a = 5
b = 6

# Manière classique
c = b
b = a
a = c

print(a, b)

# unpacking
a, b = b, a

print(a, b)