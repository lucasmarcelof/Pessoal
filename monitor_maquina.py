import psutil
import time
import os
import funcoes_banco

def get_system_usage():
    # Uso de CPU
    cpu_usage = psutil.cpu_percent(interval=2)  # Percentual de uso da CPU (1 segundo)
    
    # Uso de Memória
    memory = psutil.virtual_memory()
    memory_total = memory.total / (1024 ** 3)  # Convertendo para GB
    memory_used = memory.used / (1024 ** 3)
    memory_percent = memory.percent  # Porcentagem usada

    # Uso do Disco
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024 ** 3)  # Convertendo para GB
    disk_used = disk.used / (1024 ** 3)
    disk_percent = disk.percent  # Porcentagem usada

    # Uso da Rede
    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent / (1024 ** 2)  # Convertendo para MB
    bytes_recv = net.bytes_recv / (1024 ** 2)

    # Exibir os dados
    os.system('cls')
    funcoes_banco.data_insert_banco(cpu_usage,memory_percent,disk_used)
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_percent}%)")
    print(f"Disk Usage: {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent}%)")
    print(f"Network: {bytes_sent:.2f} MB sent, {bytes_recv:.2f} MB received")

# Loop para monitoramento contínuo
try:
    while True:
        get_system_usage()
        print("-" * 40)
        time.sleep(10)  # Atualizar a cada 5 segundos
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")
