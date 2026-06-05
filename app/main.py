from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious content
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid hostname')
    return execute_ping(host)