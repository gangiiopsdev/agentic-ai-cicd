from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = {'example.com', 'test.example.com'}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', f'-c 1 {host}'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}