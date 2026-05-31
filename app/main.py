from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run to avoid shell=True and potential command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    # Using a safe function to handle the ping command
    return {'status': 'completed', 'output': safe_ping(host)}