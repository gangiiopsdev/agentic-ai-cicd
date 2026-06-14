from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run to avoid shell=True and improve security
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function instead of subprocess.call
    status = safe_ping(host)
    return {'status': 'completed', 'output': status}