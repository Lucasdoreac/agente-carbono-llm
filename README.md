# Agente Autônomo para Análise de Carbono (com A2A e ADK)

Um sistema em Python que utiliza Modelos de Linguagem Grandes (LLMs) para realizar análises e previsões de emissões de carbono em processos industriais. Construído com um **Agent Development Kit (ADK)** para modularidade e interoperabilidade, este agente pode se comunicar com outros serviços via **Application-to-Application (A2A)** para compartilhar insights e acionar ações.

## Principais Funcionalidades

- Processamento e análise de dados de emissões de carbono (ex: CSV).
- Integração com LLMs para análise de texto e geração de previsões.
- Arquitetura de agente modular usando **ADK** para fácil extensão e adição de 'skills'.
- Interface de linha de comando (CLI) para interagir com o agente.
- Geração de relatórios sumarizando as análises e previsões.
- Publicação de eventos/resultados via **A2A** para outros sistemas (ex: dashboards, sistemas de alerta).
- Containerização com Docker.

## Como Executar

1. Clone este repositório e acesse a pasta do projeto:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/agente-carbono-llm.git
   cd agente-carbono-llm
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o agente:
   ```bash
   python src/main.py
   ```

## Integração A2A (Exemplo)

O agente pode publicar eventos em um broker ou endpoint A2A (ex: MQTT, HTTP) quando uma nova análise é concluída ou uma previsão é gerada. Outras aplicações podem se inscrever nestes eventos para automação, dashboards, alertas, etc.

## Estrutura do Projeto

```
agente-carbono-llm/
├── data/                # Dados de entrada (CSV)
├── src/
│   ├── agent.py         # Lógica principal do agente
│   ├── data_processor.py
│   ├── llm_integration.py
│   ├── a2a_publisher.py
│   └── skills/          # Skills ADK (ex: detecção de tendências)
├── tests/               # Testes automatizados
├── requirements.txt     # Dependências do projeto
├── Dockerfile           # Containerização
└── README.md            # Este arquivo
```

## Exemplo de Skill ADK

```python
def detect_trend(df):
    if df['emissao_co2_toneladas'].is_monotonic_increasing:
        return "Tendência de alta nas emissões."
    elif df['emissao_co2_toneladas'].is_monotonic_decreasing:
        return "Tendência de queda nas emissões."
    else:
        return "Sem tendência clara."
```

## Exemplo de Publicação A2A (MQTT)

```python
import paho.mqtt.publish as publish
import json

def publish_analysis_result(data):
    publish.single("carbon/analysis", json.dumps(data), hostname="localhost")
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

**Desenvolvido para promover sustentabilidade e inovação com IA.**