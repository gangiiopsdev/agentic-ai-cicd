from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        # Use os.path.abspath to ensure the full path of the executable
        response = subprocess.run([os.path.abspath('ping'), host], capture_output=True, text=True)
        return {'status': 'completed', 'output': response.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)