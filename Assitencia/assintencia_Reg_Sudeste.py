import json

# Dados organizados em um dicionário
dados = {
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
}




# Converter o dicionário para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Opcional: Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)
