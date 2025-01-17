# ETL Simples com Extração de API, Banco e Salvamento Local 🧑‍💻

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) simples, no qual eu extraio dados de uma API 🌐 e de um banco de dados simulado 💾. Depois, transformo os dados, aplicando um filtro de valores acima de 100 e um desconto de 10% 💸. Por fim, salvo os dados processados localmente em um arquivo CSV 📂. Também inclui uma verificação de integridade para garantir que não haja valores ausentes 🧐.

## Funcionalidades 🚀
- **Extração de dados:** Coleta dados de uma API externa e de um banco de dados local.
- **Transformação de dados:** Filtra os dados para manter apenas os valores acima de 100 e aplica um desconto de 10%.
- **Carregamento de dados:** Salva os dados transformados localmente em arquivos CSV.
- **Verificação de integridade:** Checa se há valores ausentes nos dados transformados.
- **Limpeza de arquivos temporários:** Limpa arquivos temporários após o processamento.

## Tecnologias Utilizadas 🛠️
- **Python:** Para automação do pipeline de ETL.
- **Pandas:** Para manipulação e transformação dos dados.
- **Requests:** Para realizar requisições HTTP à API.
- **Schedule:** Para agendar e automatizar a execução do pipeline.
