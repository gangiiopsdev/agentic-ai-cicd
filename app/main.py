from fastapi import FastAPI
import os

app = FastAPI()

def ping_host(host):
    try:
        output = os.system(f'ping {host} -c 1') == 0
        return {'status': 'completed', 'success': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_host(host)