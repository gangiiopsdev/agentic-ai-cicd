from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Use subprocess.run instead of subprocess.call for better control and security
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)