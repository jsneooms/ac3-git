import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

 limite = 1000
 numero = 2
 c = 1
 p = 0
 print "Primos: ",
 while numero < 1000:
     i = numero -1
     while i > 1:
         if numero % i == 0: break
           i -= 1
           c += 1
     else:
        print numero,
         p += 1
     numero += 1
 
print "\n\nForam encontrados %d números primos." %p
print "Foram necessárias %d comparações." %c

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

