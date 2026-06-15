from fastapi import FastAPI
import subprocess
global_config = {'ping_command': ['ping', '8.8.8.8']}

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(global_config['ping_command'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)