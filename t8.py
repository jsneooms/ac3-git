import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

x, mult = 2.0 
n = 100
lista = [] 
while (x<n):
    if (n % x == 0):
        lista.append(x)
        mult +=1
    x+=1
    else:
        if(mult==0):
            print("É primo")
        else:
            print(n"Não é primo e seus divisores não:", lista)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

