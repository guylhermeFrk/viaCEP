import requests

def main():
    print('=' * 10)
    print('Consulta CEP')
    print('=' * 10)

    cep_input = input('Digite o CEP para consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    r = requests.get(f'https://viacep.com.br/ws/{cep_input}/json')

    dados = r.json()

    if 'erro' not in dados:
        print(dados) # printa tudo
        # print(f"CEP: {dados['cep']}")
        # print(f"Logradouro: {dados['logradouro']}")
        # print(f"Complemento: {dados['complemento']}")
        # print(f"Bairro: {dados['bairro']}")
        # print(f"Cidade: {dados['localidade']}")
        # print(f"Estado: {dados['uf']}")
    else:
        print(f'O CEP {cep_input} é inválido!')

    option = int(input('\nDeseja realizar uma nova consulta? \n1. Sim\n2. Sair\n\nR: '))

    if option == 1:
        main()
    else:
        exit()


if __name__ == '__main__':
    main()