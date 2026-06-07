from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a whitelist of allowed hosts or use other validation logic
    return host in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}