from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() and e.isprintable())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or len(sanitized_host) > 100:
        raise ValueError("Invalid input for ping command")
    subprocess.run(shlex.split(f"ping -c 4 {sanitized_host}") + ['2>&1'], check=True, shell=False)
    return {"status": "completed"}