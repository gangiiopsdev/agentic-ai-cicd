from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)