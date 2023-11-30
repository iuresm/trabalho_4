from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)

@app.route('/api/calculos', methods=['POST'])
def realizar_calculos():
    dados = request.get_json()

    if 'operacao' not in dados or 'numero' not in dados:
        return jsonify({"erro": "Parâmetros ausentes"}), 400

    operacao = dados['operacao']
    numero = int(dados['numero'])

    resultado = None

    if operacao == 'fatorial':
        resultado = calcular_fatorial(numero)
    elif operacao == 'fibonacci':
        resultado = calcular_fibonacci(numero)
    else:
        return jsonify({"erro": "Operação não suportada"}), 400

    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
