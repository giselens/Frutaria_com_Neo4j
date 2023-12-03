from neo4j import GraphDatabase

url = "bolt://localhost:7687"  
user = "neo4j"            
password = "banconeo4j" 

def conexao_neo4j(url, user, password):
    return GraphDatabase.driver(url, auth=(user, password))


driver = conexao_neo4j(url, user, password)

def execute(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()

driver.close()


def lista_clientes():

    querylist = f"""MATCH (Cliente:Cliente) RETURN Cliente"""
    lista = execute(querylist)

    for record in lista:
        Cliente_node = record['Cliente']
        

        print("ID Cliente:", Cliente_node['id_cliente'])
        print("CPF:", Cliente_node['cpf'])
        print("Nome:", Cliente_node['nome'])
        print("Email:", Cliente_node['email'])
        print("Telefone:", Cliente_node['telefone'])
        print("Data de Nascimento:", Cliente_node['dt_nasc'])
       
        print("\n")


def cadastrar_cliente(id,cpf, nome, email, telefone, nascimento, id_endereco):
    if id_endereco is None:
        id_endereco_param = "NULL"
    else:
        id_endereco_param = id_endereco

    selectconsulta = f"""
    CREATE (cliente:Cliente {{id_cliente: {id} , cpf: '{cpf}', nome: '{nome}', email: '{email}', 
    telefone: '{telefone}', dt_nasc: '{nascimento}', id_endereco: {id_endereco_param}}})
    """

    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

lista_clientes()
resposta = cadastrar_cliente(4,'666666','Marta','mart@gmail.com','337733','1999-04-01',1)
print(resposta)