from fastapi import FastAPI
import subprocess
generatePingCommand = lambda host: ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = subprocess.run(generatePingCommand(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}