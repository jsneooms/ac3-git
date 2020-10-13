import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

lista_numeros = [x for x in range(101)]

lista_primos = list()

lista_divisores = [x for x in lista_numeros if x != 0]

for number in lista_numeros: 

    soma_divisores = 0 

    for divisor in lista_divisores:

        if number % divisor == 0: 
            soma_divisores += 1
        
        elif number < divisor:
            break

    if soma_divisores == 2: 
        lista_primos.append(number)

print(lista_primos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

