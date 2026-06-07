from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)