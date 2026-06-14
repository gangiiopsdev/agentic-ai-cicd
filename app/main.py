from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Safer implementation using subprocess.run with shell=False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}