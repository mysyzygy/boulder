from app import db

class Strategy:
    def __init__(self, socketio):
        self.socketio = socketio
        self.db = db


    def analyze(self, data):
        if data['data'] == 0:
            self.socketio.emit('buy_order', data)
        elif data['data'] == 1:
            self.socketio.emit('sell_order', data)

