import sqlite3
import datetime

  
# Função para criar uma tabela
def create_table():
    conn = sqlite3.connect('dbmonitoramentorecursos.db')
    c = conn.cursor() 
    c.execute('CREATE TABLE IF NOT EXISTS monitorRecursos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, cpu REAL, memoria REAL, disco REAL)')
    c.close()
    conn.close()
    

def data_insert_banco(cpu,memoria,disco):
    conn = sqlite3.connect('dbmonitoramentorecursos.db')
    c = conn.cursor()   
    new_date = datetime.datetime.now()
    c.execute("INSERT INTO monitorRecursos (date, cpu, memoria, disco) VALUES (?, ?, ?,?)", (new_date, cpu, memoria, disco))
    conn.commit()
    c.close()
    conn.close()

# Leitura de dados
def leitura_todos_dados():
    conn = sqlite3.connect('dbmonitoramentorecursos.db')
    c = conn.cursor()   
    c.execute("SELECT * FROM monitorRecursos ORDER BY id desc LIMIT 20")
    data = []
    cpu = []
    memoria = []
    disco = []
    for linha in c.fetchall():
        data.append(linha[1])
        cpu.append(linha[2])
        memoria.append(linha[3])
        disco.append(linha[4])
    c.close()
    conn.close()
    return data, cpu, memoria, disco     
