from fastapi import FastAPI
import subprocess
from urllib.parse import quote

global host_whitelist = set(['example.com', 'test.com'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in host_whitelist:
        return {'error': 'Host is not allowed'}
    # Secure implementation
    try:
        subprocess.run(['ping', '-c', '1', quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}