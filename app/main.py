from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run instead of shell=True
        try:
            subprocess.run(['ping', host], check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = SafePing.ping(host)
    if 'status' in result and result['status'] == 'failed':
        return result
    return {"status": "completed", "result": result}