from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        try:
            # Sanitize input by using a whitelist of allowed hosts
            if host not in ['example.com', 'localhost']:
                raise ValueError('Host not allowed')
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
        except ValueError as ve:
            return str(ve)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = SafeSubprocess.safe_ping(host)
    return {'status': 'completed', 'result': result}