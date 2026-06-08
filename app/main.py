from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, shell=False, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):  # Use Pydantic model validation for input sanitization
    if not host:
        return {'error': 'Host parameter is required', 'status': 'failed'}
    command = PingCommand(host)
    try:
        result = command.execute()
        return {'status': 'completed', 'output': result}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}