from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', quote(host)], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return f'Error: {str(e)}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}