from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    try:
        # Secure implementation using subprocess.run with shell=False and list of arguments
        result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)