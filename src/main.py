# src/main.py
from .agent import run_carbon_analysis_agent

if __name__ == '__main__':
    print('Iniciando Agente Autônomo para Análise de Carbono...')
    data_file_path = 'data/sample_emissions_data.csv'
    run_carbon_analysis_agent(data_file_path)
