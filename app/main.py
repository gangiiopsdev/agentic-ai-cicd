from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return {'status': 'completed', 'output': result.stdout.decode()}
            else:
                return {'status': 'failed', 'error': result.stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    return PingCommand.ping(host)