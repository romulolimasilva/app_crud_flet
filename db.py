import sqlite3

DATABASE = 'app_database.db'

def get_connection():
    return sqlite3.connect(DATABASE)

# Criar tabela para cadastro
def create_table_cadastro():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
        )
    ''')
    conn.commit()
    conn.close()
    
def inserir_cadastro(nome, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cadastro (nome, email) VALUES (?, ?)
    ''', (nome, email))
    conn.commit()
    conn.close()
    
def obter_cadastros():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email FROM cadastro')
    cadastros = cursor.fetchall()
    conn.close()
    return cadastros

def editar_cadastro(cadastro_id, nome, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE cadastro SET nome = ?, email = ? WHERE id = ?
    ''', (nome, email, cadastro_id))
    conn.commit()
    conn.close()

def deletar_cadastro(cadastro_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cadastro WHERE id = ?', (cadastro_id,))
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    create_table_cadastro()
    print("Tabela 'cadastro' criada com sucesso!")