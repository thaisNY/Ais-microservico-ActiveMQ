import stomp
import json

def send_order(order):
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect('admin', 'admin', wait=True)
    
    # Envia o pedido em formato JSON
    order_message = json.dumps(order)
    conn.send(body=order_message, destination='/queue/teste-UPE')
    print(f"Pedido enviado: {order_message}")
    
    conn.disconnect()

if __name__ == "__main__":
    # Exemplo de pedido
    order = {
        "product_id": 123,
        "quantity": 2,
        "customer": "João Silva"
    }
    send_order(order)
