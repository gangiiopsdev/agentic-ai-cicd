from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = quote(host)
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}