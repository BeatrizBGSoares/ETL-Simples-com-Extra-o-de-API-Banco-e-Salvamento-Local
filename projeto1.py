import schedule
import time
import pandas as pd
import random
import os
import logging
from datetime import datetime
import requests

logging.basicConfig(filename="processamento.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def extrair_dados_api():
    try:
        logging.info("Tentando extrair dados da API...")
        response = requests.get("https://api.exemplo.com/dados")
        response.raise_for_status()
        dados = response.json()
        logging.info("Dados extraídos da API com sucesso.")
        print("Dados extraídos da API:", dados)
        return pd.DataFrame(dados)
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao extrair dados da API: {e}")
        return pd.DataFrame()

def extrair_dados_banco():
    try:
        logging.info("Tentando extrair dados do banco de dados...")
        dados = pd.DataFrame({
            'id': [1, 2, 3],
            'valor': [120, 50, 300],
            'data': ['2025-01-15', '2025-01-16', '2025-01-17']
        })
        logging.info("Dados extraídos do banco de dados com sucesso.")
        print("Dados extraídos do banco de dados:")
        print(dados)
        return dados
    except Exception as e:
        logging.error(f"Erro ao extrair dados do banco de dados: {e}")
        return pd.DataFrame()

def transformar_dados(dados):
    try:
        logging.info("Iniciando a transformação de dados...")
        if dados.empty:
            logging.warning("Nenhum dado disponível para transformação.")
            return pd.DataFrame()
        dados_filtrados = dados[dados['valor'] > 100]
        dados_filtrados['valor_com_desconto'] = dados_filtrados['valor'] * 0.9
        logging.info("Transformação de dados realizada com sucesso.")
        print("Dados transformados:")
        print(dados_filtrados)
        return dados_filtrados
    except Exception as e:
        logging.error(f"Erro ao transformar dados: {e}")
        return pd.DataFrame()

def carregar_dados_localmente(dados):
    try:
        if dados.empty:
            logging.warning("Nenhum dado para carregar.")
            return
        arquivo_saida = f"dados_processados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        dados.to_csv(arquivo_saida, index=False)
        logging.info(f"Dados carregados localmente no arquivo {arquivo_saida}.")
        print(f"Dados salvos no arquivo {arquivo_saida}.")
    except Exception as e:
        logging.error(f"Erro ao carregar dados localmente: {e}")

def verificar_integridade(dados):
    try:
        if dados.empty:
            logging.warning("Nenhum dado para verificar.")
            return
        if dados.isnull().any().any():
            logging.warning("Dados com valores ausentes encontrados.")
            print("Dados com valores ausentes encontrados.")
        else:
            logging.info("Verificação de integridade concluída, sem valores ausentes.")
            print("Verificação de integridade concluída, sem valores ausentes.")
    except Exception as e:
        logging.error(f"Erro na verificação de integridade: {e}")

def limpar_dados_temp():
    try:
        logging.info("Limpando arquivos temporários...")
        if not os.path.exists("temp"):
            os.makedirs("temp")
        arquivos = os.listdir("temp")
        for arquivo in arquivos:
            os.remove(f"temp/{arquivo}")
        logging.info("Arquivos temporários limpos com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao limpar arquivos temporários: {e}")

def pipeline_completo():
    logging.info("Iniciando pipeline de ETL.")
    print("Iniciando pipeline de ETL...")

    dados_api = extrair_dados_api()
    dados_banco = extrair_dados_banco()

    dados_combinados = pd.concat([dados_api, dados_banco], ignore_index=True)

    dados_transformados = transformar_dados(dados_combinados)
    if not dados_transformados.empty:
        carregar_dados_localmente(dados_transformados)
        verificar_integridade(dados_transformados)
    limpar_dados_temp()

def agendar_tarefas():
    schedule.every(1).minutes.do(pipeline_completo)
    logging.info("Tarefas agendadas com sucesso.")
    print("Tarefas agendadas com sucesso.")

def main():
    agendar_tarefas()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
