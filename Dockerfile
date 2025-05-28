# Use uma imagem Python oficial como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências e instale
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["python", "src/main.py"]
