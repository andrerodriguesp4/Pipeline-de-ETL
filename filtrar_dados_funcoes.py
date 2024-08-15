import pandas as pd

def compradores(produto):
    try:
        #lê o banco de dados
        data = pd.read_csv('dados_vendas.csv')

        #checa se existe a coluna "Produto"
        if 'Produto' not in data.columns:
            return 'Erro: Coluna "Produto" não encontrada no CSV'

        #seleciona as linhas que tem o produto escolhido
        linhas_prod = data[data['Produto'] == produto]
        
        #filtra as colunas e deixa somente a coluna clientes e as transforma em uma lista
        clientes_produto = linhas_prod['Cliente'].tolist()

        #checa se a lista não está vazia
        if not clientes_produto:
            return 'Produto não encontrado'
        else:
            return list(set(clientes_produto))

    except Exception as ex:
        return f'Erro: {ex}'

def contar_qtde_produtos_vendidos(produto):
    #lê o banco de dados
    try:
        data = pd.read_csv('dados_vendas.csv')
        
        #checa se existe a coluna "Produto"
        if 'Produto' not in data.columns:
            return 'Erro: Coluna "Produto" não encontrada no CSV'

        #seleciona as linhas que tem o produto escolhido
        linhas_prod = data[data['Produto'] == produto]

        #soma a quantidade do produto que foi vendido
        soma = linhas_prod['Quantidade'].sum()

        resultado = str(soma)

        #retorna a quantidade de produtos vendidos
        return resultado

    except Exception as ex:
        return f'Erro: {ex}'

def listar_produtos():
    try:
        #lê o banco de dados
        data = pd.read_csv('dados_vendas.csv')

        #checa se a coluna "Produto" existe
        if 'Produto' not in data.columns:
            return 'Erro: Coluna "Produto" não encontrada no CSV'

        #seleciona somente a coluna "Produto" e a transforma em uma lista
        produtos = data['Produto'].tolist()

        #obtém os produtos únicos
        lista_produtos = list(set(data['Produto'].tolist()))
        
        return lista_produtos

    except Exception as ex:
        return f'Erro: {ex}'

def filtrar_compras_por_cliente(cliente):
    try:
        #lê o banco de dados
        data = pd.read_csv('dados_vendas.csv')

        if 'Cliente' not in data.columns:
            return 'Erro: Coluna "Região" não encontrada no CSV'

        #seleciona as linhas que tem o nome do cliente
        lista_compras =  data[data['Cliente'] == cliente]

        #checa se o cliente existe no banco de dados
        if lista_compras.empty:
            return 'Cliente não realizou compras'
        else:
            return lista_compras[['Cliente', 'Produto', 'Quantidade']]

    except Exception as ex:
        return f'Erro: {ex}'
    
def filtrar_clientes_por_regiao(regiao):
    try:
        #lê o banco de dados
        data = pd.read_csv('dados_vendas.csv')

        if 'Região' not in data.columns:
            return 'Erro: Coluna "Região" não encontrada no CSV'

        #seleciona as linhas que tem clientes da região solicitada
        linhas_regiao = data[data['Região'] == regiao]

        #verifica se a lista está vazia
        if linhas_regiao.empty:
            return 'Nenhuma compra foi realizada na região e/ou região inexistente'

        #seleciona o cliente, produto e quantidade
        resultado = linhas_regiao[['Cliente', 'Produto', 'Quantidade', 'Região']]

        #retorna o resultado
        return resultado

    except Exception as ex:
        return f'Erro: {ex}'

def listar_clientes():
    try:
        #lê o banco de dados
        data = pd.read_csv('dados_vendas.csv')
        #verifica se a coluna "Clientes" existe
        if 'Cliente' not in data.columns:
            return 'Erro: Coluna "Cliente" não encontrada no CSV'
        #selecionar a coluna clientes
        clientes = data['Cliente']
        #converter para lista
        lista_clientes = set(clientes.tolist())
        #converter em DataFrame
        df = pd.DataFrame(lista_clientes, columns=['Cliente'])
        return df
    except Exception as ex:
        return f'Erro: {ex}'

