from fastapi import FastAPI
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Validate and sanitize the host input to prevent unexpected behavior
            if not host or len(host) > 255:
                raise ValueError('Invalid host parameter')
            safe_host = shlex.quote(host)
            result = subprocess.run(['ping', '-c', '4', safe_host], capture_output=True, text=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    safe_ping = SafePing()
    return safe_ping.ping(host)