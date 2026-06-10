from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host):
        try:
            # Validate input more strictly
            if not host.isalnum() or len(host) > 255:
                raise ValueError('Invalid input')
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode())

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping_instance(host)}