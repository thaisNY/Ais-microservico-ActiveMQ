import stomp
import json

class ConfirmationListener(stomp.ConnectionListener):
    def on_message(self, frame):
        confirmation = json.loads(frame.body)
        print(f"Confirmação recebida: {confirmation}")

def start_confirmation_consumer():
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', ConfirmationListener())
    conn.connect('admin', 'admin', wait=True)
    
    # Se inscreve na fila inventory.queue para receber as confirmações
    conn.subscribe(destination='/queue/inventory', id=1, ack='auto')
    
    print("Aguardando confirmações de estoque...")
    input("Pressione Enter para sair\n")
    conn.disconnect()

if __name__ == "__main__":
    start_confirmation_consumer()
