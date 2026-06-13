from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host name')
    subprocess.call(['ping', shlex.quote(host)])
    return {'status': 'completed'}