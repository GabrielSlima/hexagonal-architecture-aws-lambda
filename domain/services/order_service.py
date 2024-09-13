# actual port implementation
from domain.inbound_ports.order_port import OrderPort

class OrderService(OrderPort):
    def create(self):
        raise Exception("Not implemented")
    
    def cancel(self):
        raise Exception("Not implemented")
