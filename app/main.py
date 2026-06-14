from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {"status": "completed", "output": output}