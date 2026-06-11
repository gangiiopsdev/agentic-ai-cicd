from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', quote(host)], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):     
    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}