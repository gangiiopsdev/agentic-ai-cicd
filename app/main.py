from fastapi import FastAPI
import subprocess
def execute_safe_command(command, params):
    try:
        completed_process = subprocess.run([command] + params, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return completed_process.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    params = [host]
    result = execute_safe_command('ping', params)
    return {'status': 'completed', 'result': result}