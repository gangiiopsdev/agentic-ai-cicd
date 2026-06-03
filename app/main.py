from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

def execute_ping(host):
    sanitized_host = sanitize_host(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed", "output": None}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": e.output}