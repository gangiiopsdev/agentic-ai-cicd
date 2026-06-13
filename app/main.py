from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)