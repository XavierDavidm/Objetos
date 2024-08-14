#.2
import csv
def criar_headlines(csv_file_path, txt_file_path):
    # Abre o arquivo CSV para leitura
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Lê a primeira linha (cabeçalhos)
        cabeçalhos = next(reader)
        
        # Abre o arquivo de texto para escrita
        with open(txt_file_path, mode='w', encoding='utf-8') as txtfile:
            # Cria a matriz a partir dos cabeçalhos
            matriz = f"[{', '.join(cabeçalhos)}]"
            # Escreve a matriz no arquivo de texto
            txtfile.write(matriz + '\n')

# Chama a função para criar o arquivo de texto
criar_headlines(csv_file_path, txt_file_path)