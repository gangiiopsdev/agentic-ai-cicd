from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            return subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    if 'error' in result:
        return result
    else:
        return {"status": "completed", "output": result['stdout']}