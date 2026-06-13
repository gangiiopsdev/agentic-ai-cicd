from fastapi import FastAPI
import subprocess
given_host = set(('google.com', 'github.com'))
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):

    # Safe implementation
    if host in given_host:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}
    
    return {"status": "completed"}