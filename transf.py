import os
import paramiko
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Obtém as variáveis
hostname = os.getenv("SFTP_HOST")
port = int(os.getenv("SFTP_PORT"))
username = os.getenv("SFTP_USER")
password = os.getenv("SFTP_PASS")
remote_path = os.getenv("REMOTE_PATH")
local_dir = os.getenv("LOCAL_PATH")

# === Conectar ao servidor SFTP ===
transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

# === Enviar arquivos da pasta local ===
for filename in os.listdir(local_dir):
    local_file = os.path.join(local_dir, filename)
    remote_file = os.path.join(remote_path, filename).replace("\\", "/")
    sftp.put(local_file, remote_file)
    print(f"✅ Enviado: {filename}")

# === Finalizar conexão ===
sftp.close()
transport.close()

print("✅ Upload finalizado com sucesso.")
