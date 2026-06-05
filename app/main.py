from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation with quoting the host
    subprocess.call(['ping', quote_plus(host)])

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)