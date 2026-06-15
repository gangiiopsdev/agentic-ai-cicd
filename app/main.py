from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use subprocess.run without shell=True for safer execution
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return {'status': 'completed', 'stdout': result.stdout}
    except Exception as e:
        return {'status': 'error', 'stderr': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)