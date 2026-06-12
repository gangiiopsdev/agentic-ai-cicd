from fastapi import FastAPI
import subprocess
import shlex
import os
import tempfile

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() and e.isprintable())

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            result = subprocess.run([os.path.join('/bin', 'ping'), shlex.quote(sanitized_host)], capture_output=True, text=True, check=True, cwd=temp_dir)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}