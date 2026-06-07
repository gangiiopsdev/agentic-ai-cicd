from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping_result = ping(host)
        return {"status": "completed", "result": ping_result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}