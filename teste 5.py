# string que irá ser invertida
string = "exemplo"


inverted_string = []

for i in range(len(string)-1, -1, -1):
    inverted_string.append(string[i])

final_string = "".join(inverted_string)

print(final_string)