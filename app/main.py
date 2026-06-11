from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using subprocess.run() instead of subprocess.call()
        response = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': response.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)