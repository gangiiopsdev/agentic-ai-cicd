from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run with check=True and avoid shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}