from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call with shell=True for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}