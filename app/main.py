from fastapi import FastAPI
import subprocess
git
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input and validate host format
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail='Invalid host format')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}