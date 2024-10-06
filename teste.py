import stomp

def test_connection():
    try:
        conn = stomp.Connection12([('localhost', 61616)])  # Porta 61616 do ActiveMQ
        conn.connect('admin', 'admin', wait=True)
        print("Conexão estabelecida com sucesso!")
        conn.disconnect()
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    test_connection()
