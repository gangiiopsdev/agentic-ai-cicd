from fastapi import FastAPI
import subprocess
generics = r'[a-zA-Z0-9_.-]+'  # Regex pattern to validate host
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not re.match(generics, host):
        raise ValueError('Invalid hostname')
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}