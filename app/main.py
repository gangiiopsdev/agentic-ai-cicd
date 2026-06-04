from fastapi import FastAPI
import subprocess
def secure_ping(host: str) -> str:
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)