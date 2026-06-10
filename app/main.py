from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with proper arguments
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"error": str(e)}, 400