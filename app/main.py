from fastapi import FastAPI
import os
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = os.system(f'ping -c 1 {self.host}')
            return {'status': 'completed', 'output': f'Ping command executed with exit code: {output}'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()