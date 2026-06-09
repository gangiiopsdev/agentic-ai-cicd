from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.stderr}"

def ping(host: str):
    try:
        safe_ping_result = safe_ping(host)
        return {'status': 'completed', 'result': safe_ping_result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)