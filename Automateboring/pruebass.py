
sentence = 'esta es la frase y hay que contar las vocales'
lista_vocales = ['a','e','i','o','u']

def get_count(sentence):
    contar = 0
    
    for letra in lista_vocales:
        if letra in sentence:
            contar += 1
    return contar



print(get_count(sentence))