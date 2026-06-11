from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}