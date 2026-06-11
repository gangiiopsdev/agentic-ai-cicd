from fastapi import FastAPI
import subprocess
gitcmd = ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(gitcmd, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}