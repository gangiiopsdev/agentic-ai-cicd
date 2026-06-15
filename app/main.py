from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not all(c.isalnum() or c in '.-_' for c in host):
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}