from fastapi import FastAPI
import subprocess

class SafeSubprocess:
    @staticmethod
def run(command: str):
        try:
            result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = f'ping -c 1 {host}'  # Limiting the number of pings to prevent excessive resource usage
    return {'status': SafeSubprocess.run(safe_command)}