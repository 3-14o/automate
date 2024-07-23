import requests
import time

# Defina suas credenciais de API e detalhes do servidor
API_KEY = 'Z20BLZUHRHSX8YZXC9QMOLIZAD86WHHH0UNL26TA'
SERVER_ID = '3adxu6v0fcxccw'
SCRIPT_PATH = './automate/test_script.py'

def start_server():
    # Faça uma solicitação para iniciar o servidor
    response = requests.post(
        'https://api.runpod.io/start_server',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'server_id': SERVER_ID}
    )
    if response.status_code == 200:
        print("Servidor iniciado com sucesso.")
    else:
        print("Erro ao iniciar o servidor.")
    return response.json()

def stop_server():
    # Faça uma solicitação para desligar o servidor
    response = requests.post(
        'https://api.runpod.io/stop_server',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'server_id': SERVER_ID}
    )
    if response.status_code == 200:
        print("Servidor desligado com sucesso.")
    else:
        print("Erro ao desligar o servidor.")

def execute_script():
    # Conecte-se ao servidor e execute o script
    # Você pode usar SSH ou outra forma de execução remota
    # Exemplo usando paramiko para SSH
    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('seu_endereco_ip', username='seu_usuario', password='sua_senha')
    
    # Execute o script Python no servidor
    stdin, stdout, stderr = ssh.exec_command(f'python {SCRIPT_PATH}')
    print(stdout.read().decode())
    print(stderr.read().decode())

    ssh.close()

def main():
    start_server()
    time.sleep(60)  # Espera 1 minuto para garantir que o servidor esteja ativo
    execute_script()
    stop_server()

if __name__ == "__main__":
    main()
