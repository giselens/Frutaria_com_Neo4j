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


def cadastrar_cliente(id,cpf, nome, email, telefone, nascimento):
  
    id_string = str(id)
    noc = 'cliente'+id_string
    
    selectconsulta = f"""
    CREATE ({noc}:Cliente {{id_cliente: {id} , cpf: '{cpf}', nome: '{nome}', email: '{email}', 
    telefone: '{telefone}', dt_nasc: '{nascimento}'}})
    """

    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def deletar_cadastro_de_cliente(id_cliente):
    selectconsulta = f""" MATCH (n:Cliente {{id_cliente: {id_cliente}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def cadastrar_endereco(id_endereco, rua, numero, bairro, cidade, uf):
    id_string = str(id_endereco)
    noc = 'endereco'+id_string
    selectconsulta = f"""CREATE ({noc}:Endereco{{ id_endereco: {id_endereco},rua: '{rua}', numero: {numero}, bairro:'{bairro}', cidade: '{cidade}', uf:'{uf}' }}) """
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def lista_endereco():

    querylist = f"""MATCH (Endereco:Endereco) RETURN Endereco"""
    lista = execute(querylist)

    for record in lista:
        
        Endereco_node = record['Endereco']
        

        print("Id Endereço:", Endereco_node['id_endereco'])
        print("Rua:", Endereco_node['rua'])
        print("Numero:", Endereco_node['numero'])
        print("Bairro:", Endereco_node['bairro'])
        print("Cidade:", Endereco_node['cidade'])
        print("Uf:", Endereco_node['uf'])
       
        print("\n")

def deletar_endereco(id_endereco):
    selectconsulta = f""" MATCH (n:Endereco {{id_endereco: {id_endereco}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def lista_fornecedor():

    querylist = f"""MATCH (Fornecedor:Fornecedor) RETURN Fornecedor"""
    lista = execute(querylist)

    for record in lista:
        Fornecedor_node = record['Fornecedor']
        

        print("Id do fornecedor:", Fornecedor_node['id_fornecedor'])
        print("CPF/CNPJ:", Fornecedor_node['cpf_cnpj'])
        print("Empresa:", Fornecedor_node['nome_empresa'])
        print("Telefone:", Fornecedor_node['telefone'])
        print("E-mail:", Fornecedor_node['email'])
       
        print("\n")

def cadastrar_fornecedor(id_fornecedor,cpf_cnpj, nome_empresa, telefone, email):
  
    id_string = str(id_fornecedor)
    noc = 'fornecedor'+id_string
    
    selectconsulta = f"""
    CREATE ({noc}:Fornecedor {{id_fornecedor: {id_fornecedor} , cpf_cnpj: '{cpf_cnpj}', nome_empresa: '{nome_empresa}',
    telefone: '{telefone}', email: '{email}'}})"""

    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def deletar_fornecedor(id_fornecedor):
    selectconsulta = f""" MATCH (n:Fornecedor {{id_fornecedor: {id_fornecedor}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def cadastrar_pedido(id_pedido, quant_pedido, dt_pedido):

    id_string = str(id_pedido)
    noc = 'pedido'+id_string

    selectconsulta = f"""CREATE ({noc}:Pedido{{ id_pedido: {id_pedido},quant_pedido: {quant_pedido}, dt_pedido: '{dt_pedido}'}}) """
    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def lista_pedido():

    querylist = f"""MATCH (Pedido:Pedido) RETURN Pedido"""
    lista = execute(querylist)

    for record in lista:
        Pedido_node = record['Pedido']
        

        print("Id do pedido:", Pedido_node['id_pedido'])
        print("Quantidade", Pedido_node['quant_pedido'])
        print("Data do pedido:", Pedido_node['dt_pedido'])
        
       
        print("\n")

def deletar_pedido(id_pedido):
    selectconsulta = f""" MATCH (n:Pedido {{id_pedido: {id_pedido}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def relacionamentos(id_c,id_e,no1,no2,relacionamento,campo1,campo2,entidade1,entidade2):
    
    selectconsulta = """MATCH (no1:entidade1 {campo01: id_campo1})
                    MATCH (no2:entidade2 {campo02:id_campo2})
                    MERGE (no1)-[r:relacionamento]->(no2)
                    RETURN no1, r, no2"""
    
    selectconsulta = selectconsulta.replace("no1",no1)
    selectconsulta = selectconsulta.replace("no2",no2)
    selectconsulta = selectconsulta.replace("relacionamento",relacionamento)
    selectconsulta = selectconsulta.replace("id_campo1",id_c)
    selectconsulta = selectconsulta.replace("id_campo2",id_e)
    selectconsulta = selectconsulta.replace("campo01",campo1)
    selectconsulta = selectconsulta.replace("campo02",campo2)
    selectconsulta = selectconsulta.replace("entidade1",entidade1)
    selectconsulta = selectconsulta.replace("entidade2",entidade2)
    execute(selectconsulta)

    return "OK"

def cadastrar_funcionario(matricula, cpf, nome, dt_nasc, telefone, email):
  
    matricula = str(matricula)
    noc = 'funcionario'+ matricula
    
    selectconsulta = f"""
    CREATE ({noc}:Funcionario {{matricula: {matricula} , cpf: '{cpf}', nome: '{nome}', dt_nasc:'{dt_nasc}',
                 telefone: '{telefone}', email: '{email}'}})"""

    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def lista_funcionario():

    querylist = f"""MATCH (Funcionario:Funcionario) RETURN Funcionario"""
    lista = execute(querylist)

    for record in lista:
        Funcionario_node = record['Funcionario']
        

        print("Matricula do Funcionario:", Funcionario_node['matricula'])
        print("CPF:", Funcionario_node['cpf'])
        print("Nome:", Funcionario_node['nome'])
        print("Data de Nascimento:", Funcionario_node['dt_nasc'])
        print("Telefone:",Funcionario_node['telefone'])
        print("Email:", Funcionario_node['email'])
       
        print("\n")

def deletar_funcionario(matricula):
    selectconsulta = f""" MATCH (n:Funcionario {{matricula: {matricula}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def cadastrar_produto(id_produto, nome, quant_produto, peso, preco):
  
    id_string = str(id_produto)
    noc = 'produto'+id_string
    
    selectconsulta = f"""
    CREATE ({noc}:Produto {{id_produto: {id_produto} , nome: '{nome}', quant_produto:{quant_produto},
    peso: {peso}, preco: {preco}}})"""

    execute(selectconsulta)

    feedback = "Dados inseridos com sucesso!"
    return feedback

def lista_produto():

    querylist = f"""MATCH (Produto:Produto) RETURN Produto"""
    lista = execute(querylist)

    for record in lista:
        Produto_node = record['Produto']
        

        print("Id do produto:", Produto_node['id_produto'])
        print("Nome:", Produto_node['nome'])
        print("Quantidade: ", Produto_node['quant_produto'])
        print("Peso Kg:",Produto_node['peso'])
        print("Preço R$:", Produto_node['preco'])
       
        print("\n")

def deletar_produto(id_produto):
    selectconsulta = f""" MATCH (n:Produto {{id_produto: {id_produto}}}) DETACH DELETE n"""
    execute(selectconsulta)

    feedback = "Cadastro apagado!"
    return feedback

def menu():
    print("\n")
    print("--------- MENU --------------")
    print("\n")
    print("1. Listar todos os clientes")
    print("2. Cadastrar cliente")
    print("3. Apagar cadastro de cliente")
    print("\n")
    print("--------- Produtos --------------")
    print("\n")
    print("4. Lista de produtos")
    print("5. Cadastrar produto")
    print("6. Apagar cadastro do produto")
    print("\n")
    print("--------- Fornecedores--------------")
    print("\n")
    print("7. Listar todos os fornecedores")
    print("8. Cadastrar fornecedor")
    print("9. Apagar cadastro do fornecedor")
    print("\n")
    print("--------- Pedidos --------------")
    print("\n")
    print("10 - Listar Pedidos")
    print("11 - Cadastrar Pedidos")
    print("12 - Excluir Pedido")
    print("\n")
    print("--------- Funcionários --------------")
    print("\n")
    print("13 - Listar Funcionários")
    print("14 - Cadastrar Funcionários")
    print("15 - Excluir Funcionário ")
    print("\n")
    print("--------- Endereços --------------")
    print("\n")
    print("16 - Listar endereços")
    print("17 - Excluir endereços ")
    print("\n")
    print("-----------Relatórios-----------------")
    print("18. Total de pedidos por cliente")
    print("19. Total de produtos por fornecedor")
    print("20. Total de Clientes por cidade")
    
    print("\n")

    opcao = input("Escolha a opção desejada: ")

    return opcao


def tratamentodeopcoes(opcao):
    if opcao == "1":
        lc = lista_clientes()
        return lc
    if opcao == "2":

        id = input("Código: ")

        nome = input("Nome: ")

        cpf = input("Cpf: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        nascimento = input("Data de Nascimento: ")
        print("\n------Endereço------\n")
        id_e = input("Id: endereço: ")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")


        cadastrar_endereco(id_e, rua, numero1, bairro, cidade, estado)
        ic = cadastrar_cliente(id,cpf, nome, email, telefone, nascimento)

        idc_string = str(id)
        noc = 'cliente'+idc_string
       
        ide_string = str(id_e)
        noe = 'endereco'+ide_string
        
        relacionamento = "MORA"

        relacionamentos(id,id_e,noc,noe,relacionamento,'id_cliente','id_endereco','Cliente','Endereco')

        return ic

    
    if opcao == "3":
        print("Digite o id do cliente que deseja apagar o registro:")
        id = input()
        d = deletar_cadastro_de_cliente(id)
        return d
    
    if opcao == "4":
        lp = lista_produto()
        return lp
   
    if opcao == "5":
        
        id_produto = input("ID produto: ")
        nome = input("Nome: ")
        quant_produto = input("Quantidade: ")
        peso = input("Peso Kg: ")
        preco = input("Preço R$: ")


        lp = cadastrar_produto(id_produto, nome, quant_produto, peso, preco)
        return lp
    
    if opcao == "6":

        id = input("Digite o id do produto que deseja apagar:")
        d = deletar_cadastro_de_cliente(id)
        return d
    
    if opcao == "7":
            lf = lista_fornecedor()
            return lf
    
    if opcao == "8":
        nome = input("Empresa: ")

        cpf_cnpj = input("Cpf/Cnpj: ")

        email = input("E-mail: ")

        telefone = input("Telefone: ")

        print("\n------Endereço------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        #FAZER O RESTO

    if opcao == "9":
        codigo = input("Digite o código do Fornecedor que deseja apagar:")
        dlf = deletar_fornecedor(codigo)
        return dlf
    
    if opcao == "10":
        lpd = lista_pedido()
        return lpd
    
    if opcao == "11":

        id_pedido = input("Número do Pedido: ")
        quant_pedido = input("Quantidade do Pedido: ")
        dt_pedido = input("Data do Pedido: ")
        print("\n------Endereço Para Receber Pedido------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        #FAZER O RESTO 

    if opcao == "12":

        codigo = input("Digite o código do pedido que deseja apagar:")
        dlp = deletar_pedido(codigo)
        return dlp

    if opcao == "13":
        lfunc = lista_funcionario()
        return lfunc

    if opcao == "14":

        matricula = input("Matricula: ")
        cpf_funcionario = input("Cpf do Funcionario: ")
        nome_func = input("Nome do Funcionario: ")
        dt_nasc_func = input("Data de Nascimento: ")
        telefone_func= input("Telefone ")
        email_func = input("E-mail: ")
        print("\n------Endereço Funcionario------\n")
        rua = input("Rua:")
        numero1 = input("Numero:")
        bairro = input("Bairro:")
        cidade = input("Cidade:")
        estado = input("Estado:")

        #FAZER O RESTO

    if opcao == "15":
        matricula = input("Digite a matricula do funcionário que deseja apagar:")
        dlfunc = deletar_funcionario(matricula)

        return dlfunc
    
    if opcao == "16":

       le = lista_endereco()
       return le
    
    if opcao == "17":
       le = deletar_endereco()

       return le
    
   # if opcao == "18":
    #if opcao == "19":
    #if opcao == "20":