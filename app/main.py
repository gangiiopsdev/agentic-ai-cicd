from fastapi import FastAPI
import subprocess
class ShellCommand:
    @staticmethod
def safe_ping(host: str):
        return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Ensure the host input is sanitized to prevent shell injection
    safe_host = ''.join(filter(str.isalnum, host))
    cmd = f'ping {safe_host}'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return {'host': host, 'result': result.stdout}