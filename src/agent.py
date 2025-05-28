# src/agent.py
import pandas as pd
# from google.adk import agent # Exemplo de importação para ADK do Google
from .llm_integration import get_llm_analysis
from .data_processor import load_and_process_data
from .a2a_publisher import publish_analysis_result
from .skills.skill_trend import detect_trend

# @agent.register_skill(name='analyze_carbon_emissions', description='Analisa dados de emissões de carbono e gera insights.') # Exemplo de registro de skill ADK
def run_carbon_analysis_agent(data_path):
    print('Iniciando Agente Autônomo para Análise de Carbono...')
    df = load_and_process_data(data_path)
    if df.empty:
        print('Nenhum dado para processar.')
        return

    print('Dados carregados e processados:')
    print(df.head())

    insights = get_llm_analysis(str(df.to_dict()))
    print('\n--- Análise do LLM ---')
    print(insights)
    print('--- Fim da Análise ---')

    # Skill ADK: Detecta tendência
    trend = detect_trend(df)
    print(f'Skill ADK: {trend}')

    # Publica o resultado da análise via A2A
    publish_analysis_result({'type': 'carbon_analysis_completed', 'data': insights, 'trend': trend, 'source_agent': 'agente-carbono-llm'})
    print('\nResultado da análise publicado via A2A.')

    print('Agente de análise de carbono concluiu.')
