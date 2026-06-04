from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def execute(host: str):
        if not host.strip() or ' ' in host:
            raise ValueError('Invalid host')
        return subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
class PingEndpoint:
    @staticmethod
def ping(host: str):
        try:
            result = PingCommand.execute(host)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        response = PingEndpoint.ping(host)
        return response
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}