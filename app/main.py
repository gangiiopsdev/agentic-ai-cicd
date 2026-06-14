from fastapi import FastAPI
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using a whitelist for host values
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        subprocess.run(['ping', shlex.quote(host)], check=True)
    else:
        return {'error': 'Host not allowed'}

    return {'status': 'completed'}