from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '-._')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = sp.check_output(['ping', '-c', '1', sanitized_host], stderr=sp.STDOUT, timeout=5)
        return {"status": "completed", "result": result.decode()} except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}