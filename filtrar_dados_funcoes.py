import pandas as pd

def buscar_clientes_por_produto(produto):
    data = pd.read_csv('dados_vendas.csv')
    teclado = data[data['Produto'] == produto]
    clientes_produto = teclado['Cliente'].tolist()

    if not clientes_produto:
        print("Produto não encontrado")
    else:
        print(clientes_produto)
