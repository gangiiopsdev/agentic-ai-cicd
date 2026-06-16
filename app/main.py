from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using subprocess.run with shell=False and argument parsing
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return None

@app.get("/ping")
def ping(host: str):
    # Use the safe function to avoid command injection
    output = ping_safe(host)
    if output is not None:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": "Ping failed"}