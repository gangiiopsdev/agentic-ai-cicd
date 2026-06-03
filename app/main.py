from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed", "output": result.stdout}