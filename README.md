# Scraping-MercadoLivre

Este projeto utiliza o framework **Scrapy** para realizar web scraping no site Mercado Livre. O objetivo é coletar dados de produtos disponíveis na plataforma e armazená-los em um arquivo JSONL.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.x
- Scrapy

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/jhonatanpaz95/Scraping-MercadoLivre.git
   ```
   cd Scraping-MercadoLivre
   
2. Intale as dependências necessárias:
   ```bash
   pip install -r requeriments.txt
   ```

## Executando o Scraping
Para iniciar o processo de scraping, execute o seguinte comando:
  ```bash
  scrapy crawl mercadolivre -o ../../data/data.jsonl
   ```
Este comando irá coletar os dados e salvá-los no arquivo data.jsonl na pasta data.

## Estrutura do Projeto
- coleta/: Contém os arquivos relacionados à coleta de dados.
- transformacao/: Scripts para transformação dos dados coletados.
- dashboard/: Ferramentas para visualização dos dados.
- .devcontainer/: Configurações para desenvolvimento.
- .gitignore: Arquivos e pastas a serem ignorados pelo Git.
- LICENSE: Licença do projeto (MIT).
- README.md: Este arquivo de documentação.
- requeriments.txt: Lista de dependências do projeto.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

