from fastapi import FastAPI
import subprocess
global _ping_cache = {}

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)