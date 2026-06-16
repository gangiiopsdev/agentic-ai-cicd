from fastapi import FastAPI
import socket

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input (example whitelist)
        allowed_hosts = ['127.0.0.1', '::1']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            result = s.connect_ex((host, 80)) == 0
            return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}