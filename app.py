import filtrar_dados_funcoes
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/exec_compradores', methods=['POST'])
def exec_compradores():
    try:
        produto = request.form['produto']
        resultado = filtrar_dados_funcoes.compradores(produto)
        return resultado
    except Exception as ex:
        return f'Erro: {ex}'

@app.route('/exec_quantidade_produtos_vendidos', methods=['POST'])
def exec_quantidade():
    try:
        produto = request.form['produto_qtde']
        resultado = filtrar_dados_funcoes.contar_qtde_produtos_vendidos(produto)
        if(resultado == '0'):
            return 'O produto não consta no banco de dados'
        else:
            return f'A quantidade de "{produto}" vendidos foi {resultado}'
    except Exception as ex:
        return f'Erro: {ex}'

@app.route('/exec_compras_por_cliente', methods=['POST'])
def exec_compras_por_cliente():
    try:
        cliente_compras = request.form['cliente_compras']
        resultado = filtrar_dados_funcoes.filtrar_compras_por_cliente(cliente_compras)
        try:
            result = resultado.to_html()
            return result
        except:
            return resultado
    except Exception as ex:
        return f'Erro: {ex}'


if __name__ == '__main__':
    app.run(debug=True)