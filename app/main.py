from fastapi import FastAPI
import subprocess
get_output = lambda cmd: subprocess.run(cmd.split(), capture_output=True, text=True)
app = FastAPI()
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        raise ValueError('Invalid hostname')
    output = get_output(f'ping {host}')
    return {'status': 'completed', 'output': output.stdout}