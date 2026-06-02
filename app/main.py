from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c', '1', escape_host(host)], check=True, capture_output=True, text=True)
    return {"status": "completed"}