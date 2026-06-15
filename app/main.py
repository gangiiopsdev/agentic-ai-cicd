from fastapi import FastAPI
import ping3

class PingClient:
    def __init__(self):
        self.ping_client = ping3.Ping()

app = FastAPI()
ping_client_instance = PingClient()

@app.get('/ping/{host}')
def ping(host: str):
    try:
        response_time = ping_client_instance.ping_client.ping(host)
        if response_time is not None:
            return {'status': 'completed', 'response_time': response_time}
        else:
            return {'status': 'error', 'error': 'No response'}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}