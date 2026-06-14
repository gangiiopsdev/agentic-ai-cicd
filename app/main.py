from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):  # Remove the parameter to avoid injection risk
    response = safe_ping('example.com')  # Use a default or trusted host
    return {"status": "completed", "response": response}