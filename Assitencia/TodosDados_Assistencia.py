import json

# Dados de várias empresas organizados em uma lista de dicionários
dados = [
    {
        "Região:": "Centro Oeste, DF – DISTRITO FEDERAL",
        "Nome Fantasia:": "CENTRAL ELETRONICA",
        "Razão Social:": "M. L. G. Ferreira Eletrônica",
        "Endereço:": "Q C, 07, Lote 13, Lojas 01/02, S/N",
        "Cidade:": "Brasília",
        "Bairro:": "Taguatinga Centro (Taguatinga)",
        "CEP:": "72.010-070",
        "Telefone:": "(61) 3561-2334"
    },
    {
        "Região:": "Centro Oeste, GO – GOIÁS",
        "Nome Fantasia:": "CICLON ELETRONICA",
        "Razão Social:": "Barbosa e Ventura LTDA",
        "Endereço:": "Praça Vereador Boaventura Moreira de Andrade, 148",
        "Cidade:": "Goiânia",
        "Bairro:": "Setor Leste Vila Nova",
        "CEP:": "74.640-010",
        "Telefone:": "(62) 3261-5075 / (62) 3565-4604"
    },
    {
        "Região:": "Centro Oeste, GO – GOIÁS",
        "Nome Fantasia:": "PROJESOM",
        "Razão Social:": "Projesom Comércio e Serviço LTDA",
        "Endereço:": "Rua Senador Jaime, 595, Quadra 82, Lote 08",
        "Cidade:": "Goiânia",
        "Bairro:": "Setor Campinas",
        "CEP:": "74.525-010",
        "Telefone:": "(62) 3291-5136"
    },
    {
        "Região:": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia:": "TECNO PARTS ELETRONICA",
        "Razão Social:": "E R Werlang Consertos de Equipamentos e Vendas de Componentes Eletrônicos Eireli",
        "Endereço:": "Avenida Dom Bosco, 1.130",
        "Cidade:": "Cuiabá",
        "Bairro:": "Centro Sul",
        "CEP:": "78.020-050",
        "Telefone:": "(65) 3623-4750"
    },
    {
        "Região:": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia:": "INFOTECH INFORMATICA",
        "Razão Social:": "Infotech Informática LTDA – ME",
        "Endereço:": "Avenida Marechal Dutra, 1.477",
        "Cidade:": "Rondonópolis",
        "Bairro:": "Centro – A",
        "CEP:": "78.700-110",
        "Telefone:": "(66) 3421-2388"
    },
    {
        "Região:": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia:": "ROSIVALDO DIGITAL",
        "Razão Social:": "ROSIVALDO DE AGUIAR BRITO",
        "CPF:": "17484063886",
        "Endereço:": "Rua Aziza Baracat (Lot PTE Nova), 100",
        "Cidade:": "Varzea Grande",
        "Bairro:": "Ponte Nova",
        "CEP:": "78.115-090",
        "Telefone:": "(65) 3029-6770"
    },
    {
        "Região:": "Centro Oeste, MT – MATO GROSSO",
        "Nome Fantasia:": "TECNO PARTS",
        "Razão Social:": "E. R. WERLANG - ME",
        "Endereço:": "Av. Dom Bosco, 1130",
        "Cidade:": "Cuiabá",
        "Bairro:": "Centro Sul",
        "CEP:": "78.020-050",
        "Telefone:": "(65) 3623-4750"
    },
    {
        "Região:": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia:": "SIATEC ELETRONICA",
        "Razão Social:": "Antônio Carlos Alberto Diehl",
        "CPF:": "30711797072",
        "Endereço:": "Rua Coronel Sebastião Lima, 639",
        "Cidade:": "Campo Grande",
        "Bairro:": "Jardim Monte Líbano",
        "CEP:": "79.004-600",
        "Telefone:": "(67) 3387-1203"
    },
    {
        "Região:": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia:": "ELETRONICA VIP",
        "Razão Social:": "Jara, Vilharva & Cia LTDA – ME",
        "Endereço:": "Rua Antônio Maria Coelho, 1.966",
        "Cidade:": "Campo Grande",
        "Bairro:": "Vila Cidade",
        "CEP:": "79.002-220",
        "Telefone:": "(67) 3025-2244"
    },
    {
        "Região:": "Centro Oeste, MS – MATO GROSSO DO SUL",
        "Nome Fantasia:": "ELETRONICA 2001",
        "Razão Social:": "Jadir Severino de Souza",
        "Endereço:": "Avenida Quatro, 982",
        "Cidade:": "Chapadão do Sul",
        "Bairro:": "Centro",
        "CEP:": "79.560-000",
        "Telefone:": "(67) 3562-3051"
    },
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
    },
    {
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
},
{
    "Região:": "Sudeste, ES - ESPÍRITO SANTO",
    "Nome Fantasia:": "ELETRONIA TECLADOS",
    "Razão Social:": "Maria Inete de Souza Braga Stocco",
    "Endereço:": "Rua Manoel Joaquim dos Santos, 786",
    "Cidade:": "Cariacica",
    "Bairro:": "Itaciba",
    "CEP:": "29.150-270",
    "Telefone:": "(27) 99879-6499"
},
{
    "Região:": "Sudeste, ES - ESPÍRITO SANTO",
    "Nome Fantasia:": "CTME ELETRONICA",
    "Razão Social:": "José Altair da Cruz",
    "Endereço:": "Rua Paquetá, S/N, Quadra 28, Lote 07",
    "Cidade:": "Viana",
    "Bairro:": "Nova Bethânia",
    "CEP:": "29.130-010",
    "Telefone:": "(27) 3216-67209"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "ACORDE ELETRONICA",
    "Razão Social:": "JV Eletrônica LTDA",
    "Endereço:": "Rua Padre Eustáquio, 1.620",
    "Cidade:": "Belo Horizonte",
    "Bairro:": "Carlos Prates",
    "CEP:": "30.710-580",
    "Telefone:": "(31) 3201-0528"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "ELETRONICA TELEVISATRON",
    "Razão Social:": "Fabio Almeida Dominici",
    "CPF:": "52898245615",
    "Endereço:": "Rua Umuarama, 275",
    "Cidade:": "Ipatinga",
    "Bairro:": "Caravelas",
    "CEP:": "35.164-374",
    "Telefone:": "(31) 3822-5543"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "TELEVISOM ELETRONICA",
    "Razão Social:": "Assistência Técnica Rosário LTDA",
    "Endereço:": "Rua Antônio Dias Tostes, 518",
    "Cidade:": "Juiz de Fora",
    "Bairro:": "Granbery",
    "CEP:": "36.010-370",
    "Telefone:": "(32) 3213-6742"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "LCK ELETRONICA",
    "Razão Social:": "Jose Carlos Portela",
    "CPF:": "50480995672",
    "Endereço:": "Rua Professora Rosiria Amorim Guerra, 360",
    "Cidade:": "Pirapora",
    "Bairro:": "Cidade Jardim",
    "CEP:": "39.272-286",
    "Telefone:": "(38) 99146-3565"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "ELETRONICA INFINITY",
    "Razão Social:": "Marco Antonio Moreira da Silva",
    "CPF:": "05503950674",
    "Endereço:": "Av. Asia, 323",
    "Cidade:": "Santa Luzia",
    "Bairro:": "Baronesa (Benedito)",
    "CEP:": "33.115-190",
    "Telefone:": "(31) 98790-6317 / (31) 98440-7713"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "SLP SERVIÇOS E PRODUTOS",
    "Razão Social:": "SLP Serviços Eireli",
    "Endereço:": "Rua Porto Alegre, 360",
    "Cidade:": "Uberlândia",
    "Bairro:": "Brasil",
    "CEP:": "38.400-644",
    "Telefone:": "(38) 3083-3714 / (38) 99232-1200"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "ELETRÔNICA PLANTÃO",
    "Razão Social:": "JOSE CRIVELARO FILHO",
    "Endereço:": "Av. Dr Jose Mariano, 324",
    "Cidade:": "Ponte Nova",
    "Bairro:": "Palmeiras",
    "CEP:": "66.060-147",
    "Telefone:": "(31) 3817-2117"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "RF ELETRÔNICA",
    "Razão Social:": "RODRIGO FERREIRA SILVA",
    "Endereço:": "Rua Padre Viera, 982",
    "Cidade:": "Montes Claros",
    "Bairro:": "São J. Tadeu",
    "CEP:": "39.402-778",
    "Telefone:": "(38) 9953-5849"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "SLP ASSISTENCIA",
    "Razão Social:": "SLP SERVICOS E PRODUTOS",
    "Endereço:": "Rua Porto Alegre, 360",
    "Cidade:": "Uberlândia",
    "Bairro:": "Brasil",
    "CEP:": "38.400-644",
    "Telefone:": "(34) 3083-37147 / (34) 99232-1200"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "REVISÃO ELETRÔNICA",
    "Razão Social:": "ANDY WILLIANS MATOS",
    "CPF:": "05842305674",
    "Endereço:": "Rua Dom Silvério, 89",
    "Cidade:": "Conselheiro Lafaite",
    "Bairro:": "Museu",
    "CEP:": "36.400-202",
    "Telefone:": "(31) 98494-7659"
},
{
    "Região:": "Sudeste, MG - MINAS GERAIS",
    "Nome Fantasia:": "TECNO SOM",
    "Razão Social:": "Ricardo Pereira Silva",
    "Endereço:": "Rua S. Benedito, N°432-",
    "Cidade:": "Uberaba-MG",
    "Bairro:": "São Benedito",
    "CEP:": "03.482.293.0001-89",
    "Telefone:": "(34) 3363-262 CEL (34) 99967-9214"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "MUSITEC ELETRONICA",
    "Razão Social:": "Ricardo Caetano da Silva",
    "CPF:": "44540183400",
    "Endereço:": "TV SA Rego, 453",
    "Cidade:": "Belford Roxo",
    "Bairro:": "Andrade Araújo",
    "CEP:": "26.140-550",
    "Telefone:": "(21) 2667-2659"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "SHOP ELETROLINE",
    "Razão Social:": "Eletroline Eletronica Consertos LTDA",
    "Endereço:": "Avenida Duque de Caxias, 207 – Loja C",
    "Cidade:": "Duque De Caxias",
    "Bairro:": "Centro",
    "CEP:": "25.070-070",
    "Telefone:": "(21) 4129-5486"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "ELETRONICA J R",
    "Razão Social:": "Ronaldo Justo dos Santos",
    "CPF:": "92368964720",
    "Endereço:": "Rua Doutor Laureano, 938",
    "Cidade:": "Duque de Caxias",
    "Bairro:": "Vila São Luís",
    "CEP:": "25.060-220",
    "Telefone:": "(21) 99429-8903"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "IBRAMUSIC",
    "Razão Social:": "Ibrahim Augusto de Mello Soares",
    "CPF:": "09956515744",
    "Endereço:": "Praça Olavo Bilac, 32 – Sala 202",
    "Cidade:": "Japeri",
    "Bairro:": "Engenheiro Pedreira",
    "CEP:": "26.445-010",
    "Telefone:": "(21) 99046-3335"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "ELETRONICA E OFICINA BRASILIA",
    "Razão Social:": "Eletrônica e Oficina Brasília LTDA",
    "Endereço:": "Rua Marques de Caxias, 130-A",
    "Cidade:": "Niterói",
    "Bairro:": "Centro",
    "CEP:": "24.030-050",
    "Telefone:": "(21) 2620-7308"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "ELETRONICA PLAY POWER",
    "Razão Social:": "Eletrônica Play Power LTDA",
    "Endereço:": "Rua Regente Feijó, 52, PV 1, Sala 102",
    "Cidade:": "Rio de Janeiro",
    "Bairro:": "Centro",
    "CEP:": "20.060-060",
    "Telefone:": "(21) 3970-1744"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "MGTECH INFORMATICA",
    "Razão Social:": "Marcos Leandro de Souza Bonfim",
    "CPF:": "08040629780",
    "Endereço:": "Rua Lenor, 809",
    "Cidade:": "São Gonçalo",
    "Bairro:": "Porto Velho",
    "CEP:": "24.430-150",
    "Telefone:": "(21) 99660-7031"
},
{
    "Região:": "Sudeste, RJ - RIO DE JANEIRO",
    "Nome Fantasia:": "TIME MUSIC ELETRÔNICA E COMERCIO LTDA",
    "Razão Social:": "Hiro Uesugi",
    "Endereço:": "Avenida Raimundo de Farias N°166",
    "Cidade:": "Itaboraí-R.J",
    "Bairro:": "Centro",
    "CEP:": "24.800-037",
    "Telefone:": "(21) 97502-1080"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRONICA MORELLI",
    "Razão Social:": "G. A. dos Santos Morelli",
    "Endereço:": "Avenida Campos Sales, 382",
    "Cidade:": "Americana",
    "Bairro:": "Vila Jones",
    "CEP:": "13.465-590",
    "Telefone:": "(19) 3645-6190"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "TV CENTER CONSERTOS",
    "Razão Social:": "Angelo Sironi Neto",
    "Endereço:": "Rua Siqueira Campos, 875",
    "Cidade:": "Araçatuba",
    "Bairro:": "Vila Carvalho",
    "CEP:": "16.025-275",
    "Telefone:": "(18) 3621-8465"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "STA ASSISTÊNCIA TÉCNICA",
    "Razão Social:": "STA Assistência Técnica em Som Automotivo LTDA",
    "Endereço:": "Avenida Doutor Carlos Grimaldi, 228",
    "Cidade:": "Campinas",
    "Bairro:": "Jardim Conceição",
    "CEP:": "13.091-000",
    "Telefone:": "(19) 2121-6481 ou (19) 3207-0430"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "PROGETTAUDIUM",
    "Razão Social:": "Elton Batista de Melo",
    "CPF:": "31658691890",
    "Endereço:": "Rua Xavantes, 1.240",
    "Cidade:": "Franca",
    "Bairro:": "Jardim Martins",
    "CEP:": "14.406-691",
    "Telefone:": "(16) 99146-4572"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "VGTEK ELETRONICA",
    "Razão Social:": "Nivaldo Barreto Junior",
    "CPF:": "25325112813",
    "Endereço:": "TV Batola, 17",
    "Cidade:": "Guarulhos",
    "Bairro:": "Jardim Tranquilidade",
    "CEP:": "07.051-010",
    "Telefone:": "(11) 97012-3176"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "TECHSOM ELETRONICA",
    "Razão Social:": "Jurandir Rabelo de Jesus",
    "CPF:": "29280563866",
    "Endereço:": "Rua São José do Rio Preto, 100",
    "Cidade:": "Itapevi",
    "Bairro:": "Amador Bueno",
    "CEP:": "06.680-300",
    "Telefone:": "(11) 99175-3709"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "AUDIO MACHINE",
    "Razão Social:": "Mauricio Costa de Carvalho",
    "CPF:": "35315115801",
    "Endereço:": "Avenida Luiz Manfrinato, 151",
    "Cidade:": "Itapevi",
    "Bairro:": "Centro",
    "CEP:": "06.653-100",
    "Telefone:": "(11) 9702-1351"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "LIGUE ELETRONICA",
    "Razão Social:": "Robson Fabiano Santos Pereira Ourinhos",
    "Endereço:": "Rua Paraná, 1.025",
    "Cidade:": "Ourinhos",
    "Bairro:": "Centro",
    "CEP:": "19.900-020",
    "Telefone:": "(14) 3322-5258"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "HBC ELETRONICA",
    "Razão Social:": "Henry Capeleti",
    "CPF:": "11007048840",
    "Endereço:": "Rua Ipiranga, 326",
    "Cidade:": "Piracicaba",
    "Bairro:": "Centro",
    "CEP:": "13.400-480",
    "Telefone:": "(19) 3434-2662"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRONICA MINCHIO",
    "Razão Social:": "Eletrônica Minchio Service Ltda",
    "Endereço:": "Avenida do Café, 623",
    "Cidade:": "Ribeirão Preto",
    "Bairro:": "Vila Amélia",
    "CEP:": "14.050-230",
    "Telefone:": "(16) 3632-8893"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "CONITEC",
    "Razão Social:": "Conitec Instalação, Manutenção e Suporte de Equipamentos Eletrônicos LTDA",
    "Endereço:": "Rua Alva, 262, Casa 2",
    "Cidade:": "São Paulo",
    "Bairro:": "Chácara Belenzinho",
    "CEP:": "03.377-050",
    "Telefone:": "(11) 96574-1582"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRÔNICA TECHNICS LASER",
    "Razão Social:": "Eletrônica Technics Laser LTDA",
    "Endereço:": "Rua Professor Guilherme Belfort Sabino, 814",
    "Cidade:": "São Paulo",
    "Bairro:": "Campininha",
    "CEP:": "04.678-001",
    "Telefone:": "(11) 5631-0616 / (11) 97268-9091"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "STILL SOUND",
    "Razão Social:": "Jaqueline Rocha Meira",
    "Endereço:": "Rua do Triunfo, 147",
    "Cidade:": "São Paulo",
    "Bairro:": "Santa Efigênia",
    "CEP:": "01.212-010",
    "Telefone:": "(11) 3333-6677"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "GUERRA GUITARS",
    "Razão Social:": "Vitor Augusto Guerra",
    "Endereço:": "Rua Doutor Olavo Egídio, 56",
    "Cidade:": "São Paulo",
    "Bairro:": "Santana",
    "CEP:": "02.037-005",
    "Telefone:": "(11) 2977-8758"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "EDSON MENESES",
    "Razão Social:": "Edson Silva Meneses",
    "Endereço:": "Rua Nacional, 55",
    "Cidade:": "Ubatuba",
    "Bairro:": "Centro",
    "CEP:": "11.680-000",
    "Telefone:": "(12) 99789-8870"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "NETO ELETRÔNIC",
    "Razão Social:": "JOAO LEITE DA SILVA NETO",
    "Endereço:": "Rua Gerson Franca, 6-72",
    "Cidade:": "Bauru",
    "Bairro:": "Centro",
    "CEP:": "17.015-200",
    "Telefone:": "(14) 3206-9011"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRÔNICA MORELLI",
    "Razão Social:": "G. A. DOS SANTOS MORELLI",
    "Endereço:": "Av. Campos Sales, 382",
    "Cidade:": "Americana",
    "Bairro:": "Vila Jones",
    "CEP:": "13.465-590",
    "Telefone:": "(19) 3645-6190"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "STA SOM",
    "Razão Social:": "STA ASSISTENCIA TECNICA EM SOM AUTOMOTIVO",
    "Endereço:": "Av. Carlos Grimaldi, 228",
    "Cidade:": "Campinas",
    "Bairro:": "Jardim Conceição",
    "CEP:": "13.091-000",
    "Telefone:": "(19) 2121-6481 / (19) 3207-0430"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "PROGETT AUDIUM",
    "Razão Social:": "ELTON BATISTA DE MELO",
    "Endereço:": "Rua Xavantes, 1240",
    "Cidade:": "Franca",
    "Bairro:": "Jardim Martins",
    "CEP:": "14.406-691",
    "Telefone:": "(16) 99146-4572"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRÔNICA IPIRANGA",
    "Razão Social:": "ELOI FERNANDES DE MELO",
    "Endereço:": "Rua Carioba, 223",
    "Cidade:": "Americana",
    "Bairro:": "Jardim Santana",
    "CEP:": "13.478-112",
    "Telefone:": "(19) 3407-2547 / (19) 99708-4050"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "REPARO TOTAL",
    "Razão Social:": "SEGIO DE PAULA CRUZ",
    "Endereço:": "Rua Guaracica, 16",
    "Cidade:": "São Paulo",
    "Bairro:": "Vila Curuca",
    "CEP:": "08.030-220",
    "Telefone:": "(11) 96590-8653"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRÔNICA BARBOSA",
    "Razão Social:": "JOSE NATAL BARBOSA",
    "CPF:": "05687320814",
    "Endereço:": "Rua Dr. Hugo Pereira de Abreu, 1617",
    "Cidade:": "Descalvado",
    "Bairro:": "Centro",
    "CEP:": "13.690-000",
    "Telefone:": "(19) 99185-4155"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ELETRÔNICA BAPTISTA",
    "Razão Social:": "JAIRO BAPTISTA FILHO",
    "Endereço:": "Rua Augusto Cesar Costa, 261",
    "Cidade:": "Jaboticabal",
    "Bairro:": "Parque Do Trevo",
    "CEP:": "14.871-815",
    "Telefone:": "(16) 99278-7463"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "ÁUDIO MACHINE",
    "Razão Social:": "MAURICIO COSTA DE CARVALHO",
    "CPF:": "35315115801",
    "Endereço:": "Rua Benedito D Siqueira, 170",
    "Cidade:": "Itapevi",
    "Bairro:": "Jardim Da Rainha",
    "CEP:": "06.656-540",
    "Telefone:": "(11) 97102-1351"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "BILÔ ELETRÔNICA",
    "Razão Social:": "Benjamim Augusto De Quadros",
    "Endereço:": "Rua Afonso Gabriotti N° 65",
    "Cidade:": "Sorocaba",
    "Bairro:": "Vila S. Tereza",
    "CEP:": "18.015-720",
    "Telefone:": "(15) 99789-6419"
},
{
    "Região:": "Sudeste, SP - SÃO PAULO",
    "Nome Fantasia:": "EF MOTOR",
    "Razão Social:": "EFmotor Eletro Eletrônica Ltda ME",
    "Endereço:": "PC CEL Joaquim de Arruda, N°148",
    "Cidade:": "Sorocaba",
    "Bairro:": "Alem Ponte",
    "CEP:": "18.013-130",
    "Telefone:": "(15) 3227-7898 / (15) 99750-5050"
},
{
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
    

]

# Converter a lista de dicionários para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)

print("Dados exportados com sucesso para 'dados.json'")
