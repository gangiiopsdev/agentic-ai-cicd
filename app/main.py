from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    else:
        raise ValueError("Unsafe host")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)