from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Whitelist approach for allowed hosts
            if self.host in ['allowed_host1', 'allowed_host2']:
                output = subprocess.run(['ping', self.host], capture_output=True, text=True)
                return {'status': 'completed', 'output': output.stdout}
            else:
                return {'status': 'failed', 'error': 'Host not allowed'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()