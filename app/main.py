from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'output': safe_ping(host)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}