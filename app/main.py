from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command: str):
    try:
        result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    result = run_command(command)
    return {'status': 'completed', 'output': result}