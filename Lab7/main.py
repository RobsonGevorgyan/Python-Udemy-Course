colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def new_colors(listofcolors, n):
    picked = listofcolors[:n]
    return picked

print(new_colors(colors,3))

def permutation(lista):
    for i in range(len(lista)):
        print(lista[i:])
        print(lista[:i])
    return

permutation(colors)


###################

tekst = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."


for i in range(len(tekst)):
    if (tekst[i] == "("):
        result = tekst[i+1:]

for i in range(len(result)):
    if(result[i] == ")"):
        result2 = result[:i]

print(result2)