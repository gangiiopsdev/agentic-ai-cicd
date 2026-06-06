from fastapi import FastAPI
class PingService:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input to prevent injection
            if not all(c.isalnum() or c in '-.' for c in host):
                raise ValueError('Invalid hostname')
            output = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True, timeout=10)
            return {'status': 'completed', 'output': output}
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return PingService.ping(host)