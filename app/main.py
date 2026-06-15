from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)