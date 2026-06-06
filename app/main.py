from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.strip() for arg in command.split()]

def execute_ping(host):
    ping_cmd = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(ping_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr.decode())}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)