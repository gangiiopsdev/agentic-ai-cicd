from fastapi import FastAPI
class PingService:
    @staticmethod
    def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    service = PingService()
    if validate_host(host):
        return service.ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}
def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts