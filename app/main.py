from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ip_parts = host.split('.')
        if len(ip_parts) == 4 and all(part.isdigit() for part in ip_parts):
            return SafePing.safe_ping(host)
        else:
            raise ValueError('Invalid IP address')
    except Exception as e:
        return str(e)