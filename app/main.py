from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@global_app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@global_app.post('/ping/')
def ping(host: str):
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)