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
    # Validate and sanitize the input to prevent command injection attacks
    if not host or len(host) > 255 or not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'Invalid input'}
    safe_command = f'ping -c 1 {host}'
    return {'status': SafeSubprocess.run(safe_command)}