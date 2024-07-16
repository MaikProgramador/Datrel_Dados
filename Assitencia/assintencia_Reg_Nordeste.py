import json

# Dados organizados em uma lista de dicionários
dados = [
    {
        "Região:": "Nordeste, AL - ALAGOAS",
        "Nome Fantasia:": "A & R ASSISTENCIA TECNICA",
        "Razão Social:": "Aelson Luiz da Silva",
        "CPF:": "06298305416",
        "Endereço:": "Rua Arnaldo Braga, 12 – Casa",
        "Cidade:": "Maceió",
        "Bairro:": "Cruz das Almas",
        "CEP:": "57.038-130",
        "Telefone:": "(82) 3432-7026"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "DF ELETRONICA",
        "Razão Social:": "Dilson Passos dos Santos Eireli",
        "Endereço:": "Rua Santo Antônio, S/N TV 1",
        "Cidade:": "Alagoinhas",
        "Bairro:": "Teresópolis",
        "CEP:": "48.080-130",
        "Telefone:": "(75) 3421-9957"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "ELETRONICA ESSIL",
        "Razão Social:": "Edvaldo Novaes Santiago",
        "Endereço:": "Rua Patrício Mathias, 214 – Térreo",
        "Cidade:": "Cruz das Almas",
        "Bairro:": "Centro",
        "CEP:": "44.380-000",
        "Telefone:": "(75) 3621-2743"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "AUDIO SOM",
        "Razão Social:": "Zacarias Medeiros Moreira",
        "CPF:": "162579365000",
        "Endereço:": "Rua Cristóvão Barreto, 43 – Casa",
        "Cidade:": "Feira de Santana",
        "Bairro:": "Serraria Brasil",
        "CEP:": "44.003-127",
        "Telefone:": "(75) 3489-2774"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "EVERSOM ELETRONICA PROFISSIONAL",
        "Razão Social:": "Everaldo Silva Santos",
        "CPF:": "45816301500",
        "Endereço:": "Rua Santarém, 145",
        "Cidade:": "Ilhéus",
        "Bairro:": "Conquista",
        "CEP:": "45.650-700",
        "Telefone:": "(73) 3633-6953"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "GILVAN TEC",
        "Razão Social:": "Gilvan Jose das Virgens",
        "CPF:": "66875951568",
        "Endereço:": "Rua do Saldanha, 12",
        "Cidade:": "Salvador",
        "Bairro:": "Centro",
        "CEP:": "40.020-250",
        "Telefone:": "(71) 33214469"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "TEKTRONIC ASSISTENCIA TECNICA EM ELETRONICA",
        "Razão Social:": "Ramaci de Oliveira Santos Pereira",
        "CPF:": "34649271568",
        "Endereço:": "Rua do Saldanha, 17",
        "Cidade:": "Salvador",
        "Bairro:": "Centro",
        "CEP:": "40.020-250",
        "Telefone:": "(71) 8812-8128"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "ACAD ELETRO",
        "Razão Social:": "ACAD Eletro Equipamento de Som, Iluminação Profissional e Informática LTDA",
        "Endereço:": "Avenida Dom João VI, 342 – Loja 4 – Brotas Boulevard",
        "Cidade:": "Salvador",
        "Bairro:": "Brotas",
        "CEP:": "40.285-001",
        "Telefone:": "(71) 3484-4248"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "AUDIO SYSTEM ELETRONICA",
        "Razão Social:": "Quelia Ferreira Cunha",
        "CPF:": "01681939576",
        "Endereço:": "Rua Barão do Rio Branco, 87",
        "Cidade:": "Teixeira de Freitas",
        "Bairro:": "Centro",
        "CEP:": "45.985-212",
        "Telefone:": "(73) 99985-8180"
    },
    {
        "Região:": "Nordeste, BA - BAHIA",
        "Nome Fantasia:": "PCM ELETRÔNICA",
        "Razão Social:": "EDSON CARLOS TEIXEIRA DE OLIVEIRA",
        "Endereço:": "Rua Alvaro da França Rocha, 136",
        "Cidade:": "Salvador",
        "Bairro:": "Cajazeiras IV",
        "CEP:": "41.334-320",
        "Telefone:": "(71) 3309-3044"
    },
    {
        "Região:": "Nordeste, CE - CEARÁ",
        "Nome Fantasia:": "ELETRONICA ITASOM",
        "Razão Social:": "Ricardo Rebouças Dos Santos",
        "Endereço:": "Avenida Padre Ibiapina, 1.365",
        "Cidade:": "Fortaleza",
        "Bairro:": "Jacarecanga",
        "CEP:": "60.010-690",
        "Telefone:": "(85) 3223-1856"
    },
    {
        "Região:": "Nordeste, CE - CEARÁ",
        "Nome Fantasia:": "EFICAZ REPRESENTAÇOES",
        "Razão Social:": "R & E Eficaz Comércio e Representações LTDA",
        "Endereço:": "Rua Floriano Peixoto, 1.314",
        "Cidade:": "Fortaleza",
        "Bairro:": "Centro",
        "CEP:": "60.025-130",
        "Telefone:": "(85) 3254-2110"
    },
    {
        "Região:": "Nordeste, MA - MARANHÃO",
        "Nome Fantasia:": "A E & T ASSISTENCIA ELETRONICA E TECNOLOGIA",
        "Razão Social:": "V. V. Comercio e Prestação de Serviços LTDA",
        "Endereço:": "Rua Sete de Setembro, 3.353-A",
        "Cidade:": "Imperatriz",
        "Bairro:": "Bacuri",
        "CEP:": "65.916-130",
        "Telefone:": "(99) 3014-9932"
    },
    {
        "Região:": "Nordeste, MA - MARANHÃO",
        "Nome Fantasia:": "SILVATECK",
        "Razão Social:": "M. Santos Silva Comercio e Serviços",
        "Endereço:": "Rua do Alecrim, 352 – Sala 01",
        "Cidade:": "São Luís",
        "Bairro:": "Centro",
        "CEP:": "65.010-010",
        "Telefone:": "(98) 3221-0654"
    },
    {
        "Região:": "Nordeste, PB - PARAÍBA",
        "Nome Fantasia:": "A ELETRONICA",
        "Razão Social:": "Hélio Gomes da Silva",
        "Endereço:": "Rua General João Neiva, 23",
        "Cidade:": "João Pessoa",
        "Bairro:": "Jaguaribe",
        "CEP:": "58.015-350",
        "Telefone:": "(83) 98780-6418"
    },
    {
        "Região:": "Nordeste, PB - PARAÍBA",
        "Nome Fantasia:": "TEC NEW ELETRÔNICA",
        "Razão Social:": "Irandi Alberto",
        "Endereço:": "Rua Manoel Medeiro Guedes, N°111 SL 06",
        "Cidade:": "João Pessoa PB",
        "Bairro:": "Manaira",
        "CEP:": "03.925.210.0001-89",
        "Telefone:": "(83) 3246-4148/(83) 3246-5644"
    },
    {
        "Região:": "Nordeste, PB - PARAÍBA",
        "Nome Fantasia:": "MultiAudio",
        "Razão Social:": "Reginaldo Castilhos Correa",
        "Endereço:": "R: Rua da Trindade N° 0085",
        "Cidade:": "Alem Paraíba",
        "Bairro:": "São José",
        "CEP:": "36.660-000",
        "Telefone:": "(32) 8410-8531"
    },
    {
        "Região:": "Nordeste, PE - PERNAMBUCO",
        "Nome Fantasia:": "ELETRONICA FREITAS",
        "Razão Social:": "José Roderick Ramos de Freitas",
        "Endereço:": "Rua João Conde, 123-A",
        "Cidade:": "Caruaru",
        "Bairro:": "Nossa Senhora das Dores",
        "CEP:": "55.004-220",
        "Telefone:": "(81) 3721-8877"
    },
    {
        "Região:": "Nordeste, PE - PERNAMBUCO",
        "Nome Fantasia:": "TECNISYSTEN",
        "Razão Social:": "Doriregio da Paz Barbosa Eletronica",
        "Endereço:": "Rua Projetada, 36 - Quadra 09",
        "Cidade:": "Pombos",
        "Bairro:": "Loteamento Austriclinio Carlos Lorena",
        "CEP:": "55.630-000",
        "Telefone:": "(81) 99211-1636"
    },
    {
        "Região:": "Nordeste, PE - PERNAMBUCO",
        "Nome Fantasia:": "LUMAQ",
        "Razão Social:": "Ingrid Mike de Lira",
        "Endereço:": "Rua Marquês do Herval, 166",
        "Cidade:": "Recife",
        "Bairro:": "Santo Antônio",
        "CEP:": "50.020-030",
        "Telefone:": "(81) 3224-6843"
    },
    {
        "Região:": "Nordeste, PI - PIAUÍ",
        "Nome Fantasia:": "SOUND FIX",
        "Razão Social:": "Manasses Gomes Pedreira Filho 83723510310",
        "Endereço:": "Rua General João Henrique Gaioso, 11 Quadra 41",
        "Cidade:": "Teresina",
        "Bairro:": "Saci",
        "CEP:": "64.020-200",
        "Telefone:": "(86) 99475-1160"
    },
    {
        "Região:": "Nordeste, RN - RIO GRANDE DO NORTE",
        "Nome Fantasia:": "HTEC COMERCIO E SERVIÇO",
        "Razão Social:": "Flavio Henrique Rosendo",
        "Endereço:": "Avenida Prudente De Morais, 6.478",
        "Cidade:": "Natal",
        "Bairro:": "Candelária",
        "CEP:": "59.064-630",
        "Telefone:": "(84) 2020-8080"
    },
    {
        "Região:": "Nordeste, SE - SERGIPE",
        "Nome Fantasia:": "J. ELETROMUSIC",
        "Razão Social:": "João Oliveira Junior",
        "CPF:": "00452728592",
        "Endereço:": "Rua Lourival Chagas, 465 – Casa",
        "Cidade:": "Aracaju",
        "Bairro:": "Grageru",
        "CEP:": "49.025-390",
        "Telefone:": "(79) 3022-0372"
    }
]

# Converter a lista de dicionários para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Opcional: Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)
