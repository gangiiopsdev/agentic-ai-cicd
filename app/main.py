from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)