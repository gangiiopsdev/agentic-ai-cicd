from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping', '-c', '1', host]  # Limit the number of pings to mitigate potential abuse
    return {'status': SafeSubprocess.run(safe_command)}