from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e.stderr).strip()

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    result = safe_ping(host)
    return {"status": "completed", "result": result}