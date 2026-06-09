from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.isalnum() or '.' in host:
            raise ValueError("Invalid host")
        args = shlex.split('ping -c 1 ' + host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'error', 'error': str(ve)}