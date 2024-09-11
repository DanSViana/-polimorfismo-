import classes as cl

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o email do usuário: ')
    cpf = input('Informe o cpf do usuário: ')
    profissao = input('Informe o profissão do usuário: ')
    endereco = input('Informe o endereço do usuário: ')
    telefone = input('Informe o telefone do usuário: ')

    # instância a classe pessoa fisica
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)    
    
    # entrada de dados
    nome = input('Informe o nome da empresa: ')
    email = input('Informe o email da empresa: ')
    cnpj = input('Informe o CNPJ da empresa: ')
    razao_social = input('Informe o Razão Social da empresa: ')
    telefone = input('Informe o telefone da empresa: ')
    endereço = input('Informe o endereço da empresa: ')

    # instância a classe pessoa_juridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # saída de dados
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()

