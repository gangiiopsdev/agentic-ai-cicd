from fastapi import FastAPI
import subprocess
app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host input")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}