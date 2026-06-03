from fastapi import FastAPI
import subprocess
genesis = subprocess.run(['ping', host], capture_output=True, text=True, check=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = genesis.stdout.strip()
        if genesis.returncode != 0:
            error = genesis.stderr.strip()
            raise Exception(error)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}