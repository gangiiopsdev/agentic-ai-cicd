from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': response.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)