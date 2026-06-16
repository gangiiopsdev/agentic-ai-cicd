from fastapi import FastAPI
import subprocess
git config --global url."https://${{ secrets.GITHUB_TOKEN }}:@github.com".insteadOf "https://github.com"

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}