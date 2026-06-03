from fastapi import FastAPI
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = shlex.quote(host)
        try:
            result = subprocess.run(['ping', '-c', '1', safe_host], check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.output}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = SafePing.ping(host)
    return {'status': 'completed', 'result': result}