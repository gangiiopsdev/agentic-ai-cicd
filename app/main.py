from fastapi import FastAPI
import subprocess
global ping_func

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5)
        return output.stdout
    except Exception as e:
        return str(e)

class FastAPICustom(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get('/ping')(safe_ping)

app = FastAPICustom()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}