from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            # Use subprocess.Popen for better control and avoid command injection
            process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            return {'status': 'completed' if process.returncode == 0 else 'failed', 'output': stdout, 'error': stderr}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)