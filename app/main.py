from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_command(input):
    return quote(input)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}