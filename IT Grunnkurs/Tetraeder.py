import math
h = int(input("Skriv inn en verdi for høyden: "))

a = (3/math.sqrt(6))*h # verdien til lille a

A = math.sqrt(3)*(a**2)  # Overflateareal til tetraede

V = math.sqrt(2)*(a**3)/12

print("Overflatearealet til tetraeden er: " + str(round(A, 3)))

print("Volumet til tetraeden er: " + str(round(V, 3)))