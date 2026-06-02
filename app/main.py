from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c == '.').strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, shell=False)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}