# tests/test_agent.py
import unittest
from src.agent import run_carbon_analysis_agent
from unittest.mock import patch
import os

class TestAgent(unittest.TestCase):
    def setUp(self):
        # Cria um arquivo de dados de teste temporário
        self.test_data_path = 'data/test_emissions_data.csv'
        with open(self.test_data_path, 'w') as f:
            f.write('ano,processo_industrial,emissao_co2_toneladas\n')
            f.write('2023,Teste Processo,1234\n')
            f.write('2024,Teste Processo,1250\n')

    def tearDown(self):
        # Remove o arquivo de teste após os testes
        if os.path.exists(self.test_data_path):
            os.remove(self.test_data_path)

    def test_run_carbon_analysis_agent(self):
        # Testa se o agente processa corretamente o arquivo de teste
        try:
            run_carbon_analysis_agent(self.test_data_path)
        except Exception as e:
            self.fail(f'run_carbon_analysis_agent levantou uma exceção: {e}')

    def test_publish_analysis_result_called(self):
        # Corrige o patch para o caminho absoluto correto
        with patch('src.agent.publish_analysis_result') as mock_pub:
            run_carbon_analysis_agent(self.test_data_path)
            self.assertTrue(mock_pub.called)

    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
