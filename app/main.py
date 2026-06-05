from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with check_output
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Use the safe function to avoid command injection
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}