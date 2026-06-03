from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', quote(host)], check=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}