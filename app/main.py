from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    # Sanitize input to prevent command injection
    host = ''.join(char for char in host if char.isalnum() or char in '.-')
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

@app.get("/ping")
def ping(host: str):
    return {"status": "completed", "output": safe_ping(host)}