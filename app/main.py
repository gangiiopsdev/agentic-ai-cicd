from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host input to prevent command injection
    import shlex
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host input')
    return safe_ping(host)