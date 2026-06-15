from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid input"}, 400
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500