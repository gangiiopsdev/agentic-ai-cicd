from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', quote_plus(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)