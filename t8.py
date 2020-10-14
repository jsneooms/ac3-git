import os, sys
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def is_prime(number):
    divisions = 0
    response = False
    number = int(number)
    if number:
        for i in range(1, number + 1):
            if number % i == 0:
                divisions = divisions + 1
            if divisions == 2:
                response = True
    if divisions > 2:
        response = not response
    return response
 
if __name__ == '__main__':
    while(True):
        os.system('clear')
        print 'PROGRAMA QUE VERIFICA E MOSTRA QUAIS OS NÚMEROS PRIMOS DE UM INTERVALO NUMÉRICO DE 1 ATÉ 100.'
        quantidade = int( raw_input('QUANTIDADE DE NÚMEROS A SEREM VERIFICADOS: ') )
 
        if quantidade == 0:
            break
 
        for numero in range(1, quantidade + 1):
            resposta = is_prime(numero)
            if resposta:
                print '%d => É INTEIRO' % numero
            else:
                print numero
    sys.stdin.read(1)
    os.system('clear')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)