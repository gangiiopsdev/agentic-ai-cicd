from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a safer way to ping without shell=True
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
def home(request):
    return {'message': 'Agentic Self-Healing Pipeline'}
def ping(request, host: str):
    # Validate input to prevent shell injection
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host) or host.startswith('-'):
        raise ValueError('Invalid characters in hostname')
    return safe_ping(host)
app = FastAPIApp().app