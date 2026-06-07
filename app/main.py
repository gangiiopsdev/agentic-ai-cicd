from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', cmd_quote(host)], check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)