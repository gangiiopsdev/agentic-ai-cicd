from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Ensure that the host input is sanitized or validate it
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    result = safe_ping(host)
    return {"status": "completed", "result": result}