from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping_safe(host: str):
    try:
        result = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):    
    return ping_safe(host)