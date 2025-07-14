import os
from PIL import Image

# Pastas
pasta_input = "input"
pasta_output = "output"

# Garante que a pasta de saída exista
os.makedirs(pasta_input, exist_ok=True)
os.makedirs(pasta_output, exist_ok=True)

# Percorre todos os arquivos PNG da pasta de entrada
for arquivo in os.listdir(pasta_input):
    if arquivo.lower().endswith(".png"):
        nome_base = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(pasta_output, nome_base + ".bmp")

        # Verifica se o BMP já existe
        if os.path.exists(caminho_saida):
            print(f"Ignorado (já existe): {nome_base}.bmp")
            continue  # Pula para o próximo arquivo

        # Caminho da imagem de entrada
        caminho_entrada = os.path.join(pasta_input, arquivo)

        # Abre, converte e salva como BMP
        imagem = Image.open(caminho_entrada).convert("RGB")
        imagem.save(caminho_saida, format="BMP")
        print(f"Convertido: {arquivo} -> {nome_base}.bmp")

print("Processo concluído.")
