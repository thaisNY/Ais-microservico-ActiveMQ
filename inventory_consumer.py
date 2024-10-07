import stomp
import json

class OrderListener(stomp.ConnectionListener):
    def on_message(self, frame):
        order = json.loads(frame.body)
        print(f"Pedido recebido: {order}")

        # Processa o pedido e simula a atualização do estoque
        product_id = order['product_id']
        quantity = order['quantity']
        print(f"Atualizando estoque para o produto {product_id} (quantidade: {quantity})")

        # Envia confirmação para a fila inventory.queue
        conn = stomp.Connection([('localhost', 61613)])
        conn.connect('admin', 'admin', wait=True)
        confirmation_message = json.dumps({
            "status": "success",
            "product_id": product_id,
            "quantity": quantity
        })
        conn.send(body=confirmation_message, destination='/queue/inventory')
        print(f"Confirmação enviada: {confirmation_message}")
        conn.disconnect()

def start_inventory_consumer():
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', OrderListener())
    conn.connect('admin', 'admin', wait=True)
    
    # Se inscreve na fila order.queue para receber os pedidos
    conn.subscribe(destination='/queue/teste-UPE', id=1, ack='auto')
    
    print("Aguardando pedidos...")
    input("Pressione Enter para sair\n")
    conn.disconnect()

if __name__ == "__main__":
    start_inventory_consumer()
