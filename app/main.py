from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Basic input validation
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '1', host]  # Limit the number of pings to avoid excessive resource usage
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = SafePing.safe_ping(host)
    return {'status': 'completed', 'output': output}