from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess without shell=True for safer execution
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)