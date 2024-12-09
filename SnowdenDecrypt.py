from cryptography.fernet import Fernet
import os

# Carregar a chave de criptografia
def carregar_chave():
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Descriptografar arquivos .Snowden e criar MitnickDescriptografado.txt
def descriptografar_arquivos():
    chave = carregar_chave()
    fernet = Fernet(chave)

    for arquivo in os.listdir():
        if arquivo.endswith(".Snowden"):
            with open(arquivo, "rb") as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()
            dados_descriptografados = fernet.decrypt(dados_criptografados)
            with open("MitnickDescriptografado.txt", "wb") as arquivo_original:
                arquivo_original.write(dados_descriptografados)
            os.remove(arquivo)  # Remove o arquivo criptografado

if __name__ == "__main__":
    descriptografar_arquivos()
    print("Arquivos descriptografados com sucesso!")
