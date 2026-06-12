from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.Popen
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}