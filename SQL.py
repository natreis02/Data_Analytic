# Exercícios Banco de Dados

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

import pandas as pd

# Criar a tabela "alunos"
tabela_alunos = pd.DataFrame(columns=['id', 'nome', 'idade', 'curso'])

# Exibir a tabela
print(tabela_alunos)

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
# Dados dos alunos
dados_alunos = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Natália', 'Vitor', 'Miguel', 'Edvar', 'Edna'],
    'idade': [27, 32, 10, 56, 44],
    'curso': ['Matemática Aplicada', 'Ciência da Computação', 'Engenharia Civil', 'Medicina Veterinária', 'Matemática Licenciatura']
}

# Criar a tabela "alunos" com os dados
tabela_alunos = pd.DataFrame(dados_alunos)

# Exibir a tabela sem a coluna de índices
print(tabela_alunos.to_string(index=False))

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecionar todos os registros da tabela "alunos".
import sqlite3

# Conectar ao banco de dados temporário SQLite
conexao = sqlite3.connect(':memory:')

# Inserir o DataFrame na tabela "alunos" do banco de dados
tabela_alunos.to_sql('alunos', conexao, index=False, if_exists='replace')

# Executar a consulta SQL
consulta_sql = 'SELECT * FROM alunos'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Exibir os resultados
print(resultado_consulta.to_string(index=False))

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# Selecionar o nome e a idade dos alunos com mais de 20 anos
consulta_sql = 'SELECT nome, idade FROM alunos WHERE idade > 20'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Exibir os resultados
print(resultado_consulta.to_string(index=False))

# c) Selecionar os alunos do curso de "Engenharia Civil" em ordem alfabética.
# Selecionar os alunos do curso de "Engenharia Civil" em ordem alfabética
consulta_sql = 'SELECT * FROM alunos WHERE curso = "Engenharia Civil" ORDER BY nome'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Exibir os resultados
print(resultado_consulta.to_string(index=False))

# d) Contar o número total de alunos na tabela

# Contar o número total de alunos na tabela
consulta_sql = 'SELECT COUNT(*) as total_alunos FROM alunos'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Exibir o número total de alunos
print("Número total de alunos:", resultado_consulta['total_alunos'].values[0])

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
# Atualizar a idade de Miguel para 15 anos
sql_atualizacao = 'UPDATE alunos SET idade = 15 WHERE nome = "Miguel"'
conexao.execute(sql_atualizacao)

# Exibir a tabela
print("\nTabela atualizada:")

# Exibir os resultados
print(pd.read_sql_query('SELECT * FROM alunos', conexao).to_string(index=False))

# b) Remova um aluno pelo seu ID.
# Remover a aluna "Natália"
id_nat = 1
sql_remover_natalia = f'DELETE FROM alunos WHERE id = {id_nat}'
conexao.execute(sql_remover_natalia)

# Exibir a tabela atualizada
print("\nTabela após a remoção:")
print(pd.read_sql_query('SELECT * FROM alunos', conexao).to_string(index=False))

# Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

import sqlite3
import pandas as pd

# Criar tabela
tabela_clientes = pd.DataFrame(columns=['id', 'nome', 'idade', 'saldo'])

# Exibir a tabela
print("Tabela 'clientes':")
print(tabela_clientes)

# Dados dos clientes
dados_clientes = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Miliene', 'Bárbara', 'Giulia', 'Anna', 'Patrícia'],
    'idade': [22, 28, 24, 23, 23],
    'saldo': [2540.45, 500.25, 1200.75, 300.80, 800.60]
}

# Inserir os dados na tabela
tabela_clientes = pd.DataFrame(dados_clientes)

# Conectar ao banco de dados temporário SQLite
conexao = sqlite3.connect(':memory:')

# Inserir o DataFrame na tabela
tabela_clientes.to_sql('clientes', conexao, index=False, if_exists='replace')

# Exibir a tabela
print("\nTabela 'clientes':")
print(pd.read_sql_query('SELECT * FROM clientes', conexao).to_string(index=False))

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# Inserir o DataFrame na tabela do banco de dados
tabela_clientes.to_sql('clientes', conexao, index=False, if_exists='replace')

# Exibir os clientes com idade superior a 30 anos
consulta_sql = 'SELECT nome, idade FROM clientes WHERE idade > 30'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Resultados
print(resultado_consulta)

# b) Calcule o saldo médio dos clientes

# Saldo médio dos clientes
consulta_sql = 'SELECT AVG(saldo) as saldo_medio FROM clientes'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Resultado
print("Saldo médio dos clientes:", resultado_consulta['saldo_medio'].values[0])

# c) Encontre o cliente com o saldo máximo.

# Encontrar o cliente com o saldo máximo
consulta_sql = 'SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Resultado
print("Cliente com o saldo máximo:")
print(resultado_consulta.to_string(index=False))

# d) Conte quantos clientes têm saldo acima de 1000

# Clientes que têm saldo acima de 1000
consulta_sql = 'SELECT COUNT(*) as quantidade FROM clientes WHERE saldo > 1000'
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)

# Exibir o resultado
print("Quantidade de clientes com saldo acima de 1000:", resultado_consulta['quantidade'].values[0])

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

# Atualizar o saldo de um cliente (Bárbara)
consulta_sql_atualizacao_saldo = 'UPDATE clientes SET saldo = 1500.00 WHERE nome = "Bárbara"'
conexao.execute(consulta_sql_atualizacao_saldo)

# Exibir a tabela após a atualização
print("\nTabela após a atualização:")
print(pd.read_sql_query('SELECT * FROM clientes', conexao).to_string(index=False))

# b) Remova um cliente pelo seu ID.

# Remover a cliente "Milene"
id_milene = 1
consulta_sql_remocao_milene = f'DELETE FROM clientes WHERE id = {id_milene}'
conexao.execute(consulta_sql_remocao_milene)

# Exibir a tabela após a remoção
print("\nTabela após a remoção:")
print(pd.read_sql_query('SELECT * FROM clientes', conexao).to_string(index=False))

# Junção de Tabelas Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
import sqlite3
import pandas as pd

# Dados dos clientes
dados_clientes = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Miliene', 'Bárbara', 'Giulia', 'Anna', 'Patrícia'],
    'idade': [22, 28, 24, 23, 23],
    'saldo': [2540.45, 500.25, 1200.75, 300.80, 800.60]
}


# Dados das compras
dados_compras = {
    'id': [1, 2, 3, 4, 5],
    'cliente_id': [1, 2, 3, 4, 5],
    'produto': ['Guarda roupa', 'Air Fryer', 'Microondas', 'Máquina de Lavar', 'Aspirador de pó'],
    'valor': [600.00, 450.00, 350.00, 1020.00, 280.50]
}

# Criar as tabelas "clientes" e "compras"
tabela_clientes = pd.DataFrame(dados_clientes)
tabela_compras = pd.DataFrame(dados_compras)

# Conectar ao banco de dados temporário SQLite
conexao = sqlite3.connect(':memory:')

# Inserir os DataFrames nas tabelas "clientes" e "compras" do banco de dados
tabela_clientes.to_sql('clientes', conexao, index=False, if_exists='replace')
tabela_compras.to_sql('compras', conexao, index=False, if_exists='replace')

# Exibir a tabela "clientes"
print("Tabela 'clientes':")
print(pd.read_sql_query('SELECT * FROM clientes', conexao).to_string(index=False))

# Exibir a tabela "compras"
print("\nTabela 'compras':")
print(pd.read_sql_query('SELECT * FROM clientes', conexao).to_string(index=False))

# Consulta para exibir o nome do cliente, o produto e o valor de cada compra
consulta_sql = '''
    SELECT c.nome as cliente, co.produto, co.valor
    FROM clientes c
    JOIN compras co ON c.id = co.cliente_id
'''

# Exibir o resultado da consulta
resultado_consulta = pd.read_sql_query(consulta_sql, conexao)
print("\nResultado da consulta:")
print(resultado_consulta.to_string(index=False))


