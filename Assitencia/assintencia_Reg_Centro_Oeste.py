import json

# Dados de várias empresas organizados em uma lista de dicionários
dados = [
    {
        "Região": "Centro Oeste, DF – DISTRITO FEDERAL",
        "Nome Fantasia": "CENTRAL ELETRONICA",
        "Razão Social": "M. L. G. Ferreira Eletrônica",
        "Endereço": "Q C, 07, Lote 13, Lojas 01/02, S/N",
        "Cidade": "Brasília",
        "Bairro": "Taguatinga Centro (Taguatinga)",
        "CEP": "72.010-070",
        "Telefone": "(61) 3561-2334"
    },
    {
        "Região": "Centro Oeste, GO – GOIÁS",
        "Nome Fantasia": "CICLON ELETRONICA",
        "Razão Social": "Barbosa e Ventura LTDA",
        "Endereço": "Praça Vereador Boaventura Moreira de Andrade, 148",
        "Cidade": "Goiânia",
        "Bairro": "Setor Leste Vila Nova",
        "CEP": "74.640-010",
        "Telefone": "(62) 3261-5075 / (62) 3565-4604"
    },
    {
        "Região": "Centro Oeste, GO – GOIÁS",
        "Nome Fantasia": "PROJESOM",
        "Razão Social": "Projesom Comércio e Serviço LTDA",
        "Endereço": "Rua Senador Jaime, 595, Quadra 82, Lote 08",
        "Cidade": "Goiânia",
        "Bairro": "Setor Campinas",
        "CEP": "74.525-010",
        "Telefone": "(62) 3291-5136"
    },
    {
        "Região": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia": "TECNO PARTS ELETRONICA",
        "Razão Social": "E R Werlang Consertos de Equipamentos e Vendas de Componentes Eletrônicos Eireli",
        "Endereço": "Avenida Dom Bosco, 1.130",
        "Cidade": "Cuiabá",
        "Bairro": "Centro Sul",
        "CEP": "78.020-050",
        "Telefone": "(65) 3623-4750"
    },
    {
        "Região": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia": "INFOTECH INFORMATICA",
        "Razão Social": "Infotech Informática LTDA – ME",
        "Endereço": "Avenida Marechal Dutra, 1.477",
        "Cidade": "Rondonópolis",
        "Bairro": "Centro – A",
        "CEP": "78.700-110",
        "Telefone": "(66) 3421-2388"
    },
    {
        "Região": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia": "ROSIVALDO DIGITAL",
        "Razão Social": "ROSIVALDO DE AGUIAR BRITO",
        "CPF": "17484063886",
        "Endereço": "Rua Aziza Baracat (Lot PTE Nova), 100",
        "Cidade": "Varzea Grande",
        "Bairro": "Ponte Nova",
        "CEP": "78.115-090",
        "Telefone": "(65) 3029-6770"
    },
    {
        "Região": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia": "TECNO PARTS",
        "Razão Social": "E. R. WERLANG - ME",
        "Endereço": "Av. Dom Bosco, 1130",
        "Cidade": "Cuiabá",
        "Bairro": "Centro Sul",
        "CEP": "78.020-050",
        "Telefone": "(65) 3623-4750"
    },
    {
        "Região": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia": "SIATEC ELETRONICA",
        "Razão Social": "Antônio Carlos Alberto Diehl",
        "CPF": "30711797072",
        "Endereço": "Rua Coronel Sebastião Lima, 639",
        "Cidade": "Campo Grande",
        "Bairro": "Jardim Monte Líbano",
        "CEP": "79.004-600",
        "Telefone": "(67) 3387-1203"
    },
    {
        "Região": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia": "ELETRONICA VIP",
        "Razão Social": "Jara, Vilharva & Cia LTDA – ME",
        "Endereço": "Rua Antônio Maria Coelho, 1.966",
        "Cidade": "Campo Grande",
        "Bairro": "Vila Cidade",
        "CEP": "79.002-220",
        "Telefone": "(67) 3025-2244"
    },
    {
        "Região": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia": "ELETRONICA 2001",
        "Razão Social": "Jadir Severino de Souza",
        "Endereço": "Avenida Quatro, 982",
        "Cidade": "Chapadão do Sul",
        "Bairro": "Centro",
        "CEP": "79.560-000",
        "Telefone": "(67) 3562-3051"
    },
    

]

# Converter a lista de dicionários para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)

print("Dados exportados com sucesso para 'dados.json'")
