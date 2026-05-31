from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with exit code {e.returncode}: {e.stderr}"

class SafePing:
    @staticmethod
def safe_execute(host: str):
        allowed_hosts = ['google.com', 'example.com']
        if host in allowed_hosts:
            command = f'ping {host}'
            output = execute_command(command)
            return {'status': 'completed', 'output': output}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_execute(host)