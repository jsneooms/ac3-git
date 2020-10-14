import os
from flask import Flask, jsonify, request

app = Flask(__name__)

def ehDivisivel(n, d):
    return n % d == 0

def ehPrimo(n):
    for d in range(2, n):
        if (ehDivisivel(n, d)):
            return False
    return True

@app.route("/")
def primos():
    q = 100
    c = 0
    n = 2
    resultado = ""
    while c < q:
        if ehPrimo(n):
            c += 1
            resultado = resultado + str(n) + ", "
        n += 1
    return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)