from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid input"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}