import os
from PIL import Image

# Pastas de entrada e saída
pasta_input = "input"
pasta_output = "output"

# Criar pasta de saída se não existir
os.makedirs(pasta_input, exist_ok=True)
os.makedirs(pasta_output, exist_ok=True)

# Listar todos os arquivos da pasta input
for arquivo in os.listdir(pasta_input):
    if arquivo.lower().endswith(".png"):
        caminho_entrada = os.path.join(pasta_input, arquivo)

        # Abrir e converter imagem
        imagem = Image.open(caminho_entrada).convert("RGB")

        # Nome do novo arquivo (com extensão .bmp)
        nome_base = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(pasta_output, nome_base + ".bmp")

        # Salvar como BMP 24 bits
        imagem.save(caminho_saida, format="BMP")
        print(f"Convertido: {arquivo} -> {nome_base}.bmp")

print("Conversão concluída.")
