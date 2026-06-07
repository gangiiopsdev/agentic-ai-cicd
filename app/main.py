from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in '-.:/')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or len(sanitized_host) > 255:
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', sanitized_host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode('utf-8'), "stderr": result.stderr.decode('utf-8')}