import requests
import json

# URL do endpoint A2A (pode ser um Message Broker, outro serviço, etc.)
A2A_ENDPOINT = 'http://localhost:8080/a2a-events' # Exemplo

def publish_analysis_result(data):
    try:
        response = requests.post(A2A_ENDPOINT, json=data)
        response.raise_for_status() # Lança exceção para status de erro HTTP
        print(f'Evento A2A publicado com sucesso: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao publicar evento A2A: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
