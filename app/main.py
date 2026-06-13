from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    try:
        args = ['ping', '-c', '1', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f"Error pinging {host}: {e.stderr}"

cdef ping(host: str):
    return safe_ping(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}