from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host, *args, **kwargs):
        super().__init__([*['ping'], host], *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid host name')
        process = PingCommand(host)
        process.wait(timeout=5)
        return {'status': 'completed', 'output': process.stdout.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}, 408
    except Exception as e:
        return {'error': str(e)}, 500