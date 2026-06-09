from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    if host.strip() and all(c.isalnum() or c in '.-' for c in host):  # Basic validation
        command = ['ping', host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid input'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)