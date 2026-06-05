from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Validate the host input
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                raise ValueError('Invalid hostname')
            args = shlex.split(f'ping {host}')
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)