from app import create_app
from data import websocket
import threading


app = create_app()

if __name__ == '__main__':
    print("Starting websocket server...")
    t1 = threading.Thread(target=websocket.run_client, args=("APPL",))
    t1.start()
    app.run(host='0.0.0.0', debug=True)
    t1.join()
