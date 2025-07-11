import os
import time
import glob
import shutil

download_dir = os.path.abspath("C:\\Users\\gbarbosa\\Downloads\\teste")

def esperar_download_concluir(pasta, timeout=30):
    tempo = 0
    while tempo < timeout:
        arquivos_tmp = [f for f in os.listdir(pasta) if f.endswith(".tmp") or f.endswith(".crdownload")]
        if not arquivos_tmp:
            return True
        time.sleep(1)
        tempo += 1
    return False

def renomear_arquivo_baixado(pasta, novo_nome):
    arquivos = sorted(
        glob.glob(os.path.join(pasta, "*")),
        key=os.path.getctime,
        reverse=True
    )
    for arquivo in arquivos:
        if not arquivo.endswith((".tmp", ".crdownload")):
            extensao = os.path.splitext(arquivo)[1]
            novo_caminho = os.path.join(pasta, novo_nome + extensao)
            shutil.move(arquivo, novo_caminho)
            return novo_caminho
    return None
