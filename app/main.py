from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a list instead of shell=True for safety and quote host to avoid command injection
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

def validate_host(host: str):
    if '&&' in host or ';' in host or '|' in host or '`' in host:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return {'status': safe_ping(host)}