from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

@app.get="/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}