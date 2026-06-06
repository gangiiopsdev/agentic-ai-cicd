from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation with quoting the host
    subprocess.call(['ping', quote_plus(host)])

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', quote_plus(host)], capture_output=True, text=True)
        return {'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}