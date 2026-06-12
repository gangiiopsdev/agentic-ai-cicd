from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}

app = FastAPI()

@app.get('/')</code>
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    # Validate the host to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host parameter'}
    response = SafePing.ping(host)
    return response