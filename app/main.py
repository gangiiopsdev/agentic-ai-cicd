from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}