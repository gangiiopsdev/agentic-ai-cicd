from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str): return {'status': subprocess.call(['ping', safe_ping(host)])}