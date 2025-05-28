# src/agent.py
import pandas as pd
from .llm_integration import get_llm_analysis
from .data_processor import load_and_process_data

def run_carbon_analysis_agent(data_path):
    df = load_and_process_data(data_path)
    if df.empty:
        print('Nenhum dado para processar.')
        return

    print('Dados carregados e processados:')
    print(df.head())

    # Exemplo de como poderia ser uma análise com LLM
    # Aqui você passaria os dados relevantes para o LLM
    insights = get_llm_analysis(str(df.to_dict()))
    print('\n--- Análise do LLM ---')
    print(insights)
    print('--- Fim da Análise ---')

    # Aqui viria a lógica de previsão e outras funcionalidades
    print('\nAgente de análise de carbono concluiu (simulação).')
