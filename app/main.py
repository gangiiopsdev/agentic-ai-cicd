from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)