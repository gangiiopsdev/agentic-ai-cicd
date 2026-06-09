from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', *shlex.split(host)]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Error pinging {host}: {error.decode()}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed", "output": output.decode() if 'output' in locals() else ''}