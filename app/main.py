from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', quote_plus(host)], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}