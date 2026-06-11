from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    args = shlex.split(f"ping {safe_host}")
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}