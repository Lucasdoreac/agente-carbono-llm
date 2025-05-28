# src/data_processor.py
import pandas as pd

def load_and_process_data(file_path):
    try:
        df = pd.read_csv(file_path)
        # Adicione aqui lógicas de pré-processamento se necessário
        print(f'Dados carregados de {file_path}')
        return df
    except FileNotFoundError:
        print(f'Erro: Arquivo não encontrado em {file_path}')
        return pd.DataFrame()
