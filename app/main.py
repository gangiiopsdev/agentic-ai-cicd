from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host):
        # Using a list for the command avoids shell injection risks
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.strip().isalnum() or len(host) > 255:
        return {'status': 'error', 'result': 'Invalid host'}
    result = PingCommand.execute(host)
    return {'status': 'completed', 'result': result}