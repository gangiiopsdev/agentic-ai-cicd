from fastapi import FastAPI
import subprocess
getoutput = lambda x: subprocess.getoutput(x)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = getoutput(f'ping {host}')
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}