import json

# Dados organizados em um dicionário
dados = {
    "Região:": "Norte, PA - PARÁ",
    "Nome Fantasia:": "ELETRONICA TELESOM",
    "Razão Social:": "Almir Carvalho Soares Eireli",
    "Endereço:": "Avenida dos Pinheiros esquina com Rua Virgilia Rosa, S/N, Lote 02, Quadra02",
    "Cidade:": "Canaã dos Carajás",
    "Bairro:": "Jardim América",
    "CEP:": "68.537-000",
    "Telefone:": "(94) 99151-6818"
},
{
    "Região:": "Norte, PA - PARÁ",
    "Nome Fantasia:": "CSTE COMERCIO E SERVICOS",
    "Razão Social:": "Orivaldo Silva Coelho 35577002249",
    "Endereço:": "Rua Boa Ventura da Silva, 2.188",
    "Cidade:": "Belém",
    "Bairro:": "Fatima",
    "CEP:": "66.060-147",
    "Telefone:": "(91) 3119-4056 / (91) 98166-5912"
},
{
    "Região:": "Norte, RO - RONDÔNIA",
    "Nome Fantasia:": "ELETRONICA GLOBO",
    "Razão Social:": "Onofre Martins da Costa",
    "Endereço:": "Avenida Tancredo Neves, 6.023",
    "Cidade:": "Vilhena",
    "Bairro:": "Jardim Eldorado",
    "CEP:": "76.980-000",
    "Telefone:": "(69) 3321-4753 / (69) 8483-4784"
},
{
    "Região:": "Norte, RO - RONDÔNIA",
    "Nome Fantasia:": "ELETRÔNICAS CAMERAS.COM",
    "Razão Social:": "Colares Comercio e serviços LTDA",
    "Endereço:": "Rua João Goulart, 2061",
    "Cidade:": "Porto Velho",
    "Bairro:": "São Cristóvão",
    "CEP:": "76.804-034",
    "Telefone:": "(69) 99959-1328"
}


# Converter o dicionário para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Opcional: Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)
