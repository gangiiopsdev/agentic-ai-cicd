from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)