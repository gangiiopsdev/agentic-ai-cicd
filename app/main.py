from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Add validation logic for the host parameter
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": output.decode('utf-8')}