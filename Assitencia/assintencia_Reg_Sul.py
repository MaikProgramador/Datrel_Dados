import json

# Dados organizados em um dicionário
dados = {
    "Região:": "Sul, PR - PARANÁ",
    "Nome Fantasia:": "SOM PRO",
    "Razão Social:": "A Música Viva Eletronica LTDA",
    "Endereço:": "Rua Lamenha Lins, 1.130",
    "Cidade:": "Curitiba",
    "Bairro:": "Rebouças",
    "CEP:": "80.220-080",
    "Telefone:": "(41) 3248-4338"
},
{
    "Região:": "Sul, PR - PARANÁ",
    "Nome Fantasia:": "ELETRONICA DO VOVÔ",
    "Razão Social:": "Valdir Trindade",
    "CPF:": "32116969972",
    "Endereço:": "Rua Padre Antonio Patui, 28",
    "Cidade:": "Toledo",
    "Bairro:": "Jardim Santa Maria",
    "CEP:": "85.903-090",
    "Telefone:": "(45) 99974-0252"
},
{
    "Região:": "Sul, RS - RIO GRANDE DO SUL",
    "Nome Fantasia:": "T & G COMERCIO E ELETRONICA",
    "Razão Social:": "Tauana Rodrigues Bruxel",
    "Endereço:": "Rua Florença, 466",
    "Cidade:": "Novo Hamburgo",
    "Bairro:": "Canudos",
    "CEP:": "93.542-060",
    "Telefone:": "(51) 98116-5300"
},
{
    "Região:": "Sul, RS - RIO GRANDE DO SUL",
    "Nome Fantasia:": "ELETRON ASSISTENCIA TECNICA",
    "Razão Social:": "Eletron Assistência Técnica LTDA",
    "Endereço:": "Rua Morom, 724, Sala 01",
    "Cidade:": "Passo Fundo",
    "Bairro:": "Centro",
    "CEP:": "99.010-030",
    "Telefone:": "(54) 3045-1278"
},
{
    "Região:": "Sul, RS - RIO GRANDE DO SUL",
    "Nome Fantasia:": "AM ELETRONICA",
    "Razão Social:": "Almicar da Cruz da Frota 02418337014",
    "Endereço:": "Rua Dr. Bruno Chaves, 83 A",
    "Cidade:": "Pelotas",
    "Bairro:": "Três Vendas",
    "CEP:": "96.055-040",
    "Telefone:": "(53) 9845-9422 / (53) 98111-7758"
},
{
    "Região:": "Sul, RS - RIO GRANDE DO SUL",
    "Nome Fantasia:": "ELETRONICA ROQUILO - CENTRO",
    "Razão Social:": "Marcelo de Oliveira Lewis",
    "Endereço:": "Avenida Alberto Bins, 308, Conj. 20",
    "Cidade:": "Porto Alegre",
    "Bairro:": "Centro",
    "CEP:": "90.030-140",
    "Telefone:": "(51) 3221-4997"
},
{
    "Região:": "Sul, RS - RIO GRANDE DO SUL",
    "Nome Fantasia:": "GSO EFFECTS LINE ELETRÔNICA",
    "Razão Social:": "OLIVEIRA E OLIVEIRA PPAC LTDA",
    "Endereço:": "RUA VENANCIO AIRES N°1714",
    "Cidade:": "CANOAS",
    "Bairro:": "NITEROI",
    "CEP:": "92.110.000",
    "Telefone:": "(51) 3475-5066"
},
{
    "Região:": "Sul, SC - SANTA CATARINA",
    "Nome Fantasia:": "ELETRONICA OFICINA DO SOM",
    "Razão Social:": "Eduardo Passos dos Santos Vieira",
    "CPF:": "05007520950",
    "Endereço:": "Rodovia João Gualberto Soares, 1.570, Loja 03",
    "Cidade:": "Florianópolis",
    "Bairro:": "Ingleses do Rio Vermelho",
    "CEP:": "88.058-300",
    "Telefone:": "(48) 3209-4070"
},
{
    "Região:": "Sul, SC - SANTA CATARINA",
    "Nome Fantasia:": "CONSERTOS COELHO",
    "Razão Social:": "Charles Clovis Coelho",
    "CPF:": "02960119916",
    "Endereço:": "Rua Barão do Rio Branco, 1.042",
    "Cidade:": "Rodeio",
    "Bairro:": "Centro",
    "CEP:": "89.136-000",
    "Telefone:": "(47) 99737-2719"
}





# Converter o dicionário para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Opcional: Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)
