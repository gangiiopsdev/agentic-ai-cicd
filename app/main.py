from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Using subprocess.run without shell=True for a safer approach
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get="/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}