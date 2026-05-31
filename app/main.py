from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get="/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}