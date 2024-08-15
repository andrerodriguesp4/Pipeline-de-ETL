import filtrar_dados_funcoes
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/exec_compradores', methods=['POST'])
def exec_compradores():
    try:
        produto = request.form['produto']
        resultado = filtrar_dados_funcoes.compradores(produto)

        if isinstance(resultado, str):
            result = resultado
        else:
            #converter para dataframe
            df = pd.DataFrame(resultado, columns=['Clientes'])
            #converter para html
            result = df.to_html()

        return render_template('result.html', result=result)
    except Exception as ex:
        result = f'Erro: {ex}'
        return render_template('result.html', result=result)

@app.route('/exec_quantidade_produtos_vendidos', methods=['POST'])
def exec_quantidade():
    try:
        produto = request.form['produto_qtde']
        resultado = filtrar_dados_funcoes.contar_qtde_produtos_vendidos(produto)
        if(resultado == '0'):
            result = 'O produto não consta no banco de dados'
        else:
            result = f'A quantidade de "{produto}" vendidos foi {resultado}'
        return render_template('result.html', result=result)
    except Exception as ex:
        return f'Erro: {ex}'

@app.route('/exec_compras_por_cliente', methods=['POST'])
def exec_compras_por_cliente():
    try:
        cliente_compras = request.form['cliente_compras']
        resultado = filtrar_dados_funcoes.filtrar_compras_por_cliente(cliente_compras)
        try:
            result = resultado.to_html()
        except:
            result = resultado
        return render_template('result.html', result=result)
    except Exception as ex:
        result = f'Erro: {ex}'
        return render_template('result.html', result=result)

@app.route('/exec_clientes_por_regiao', methods=['POST'])
def exec_clientes_por_regiao():
    try:
        regiao_cliente = request.form['regiao']
        resultado = filtrar_dados_funcoes.filtrar_clientes_por_regiao(regiao_cliente)

        if isinstance(resultado, str):
            return render_template('result.html', result=resultado)

        result = resultado.to_html()
        return render_template('result.html', result=result)
    except Exception as ex:
        result = f'Erro: {ex}'
        return render_template('result.html', result=result)

@app.route('/exec_listar_produtos', methods=['POST'])
def exec_listar_produtos():
    try:
        resultado = filtrar_dados_funcoes.listar_produtos()

        #converter para dataframe
        df = pd.DataFrame(resultado, columns=['Produtos'])

        #convertendo para html
        result = df.to_html()

        return render_template('result.html', result=result)
    except Exception as ex:
        result = f'Erro: {ex}'
        return render_template('result.html', result=result)

@app.route('/exec_listar_clientes', methods=['POST'])
def exec_listar_clientes():
    try:
        resultado = filtrar_dados_funcoes.listar_clientes()
        #converter dataframe para html
        result = resultado.to_html()
        return render_template('result.html', result=result)
    except Exception as ex:
        result = f'Erro: {ex}'
        return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)