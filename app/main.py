from fastapi import FastAPI
import re
def ping(host: str):
    # Sanitize host input to avoid shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get('/ping')
def ping_endpoint(host: str): return ping(host)