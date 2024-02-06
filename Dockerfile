# Gebruik een officiële Python runtime als een ouder image
FROM python:3.12.1-slim

# Stel de werkmap in de container in
WORKDIR /app

# Kopieer de vereisten en installeer Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van je applicatiecode
COPY . .

# Maak de poort vrij waarop de applicatie draait
EXPOSE 8888

# Definieer het commando om de applicatie te starten
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
