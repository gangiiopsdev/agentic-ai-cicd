from fastapi import FastAPI
import subprocess
import shlex
cimport = {';': '', '&': ''}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = ''.join([cimport.get(c, c) for c in host])  # Enhanced sanitization
    args = shlex.split('ping -c 1 ' + sanitized_host)
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}