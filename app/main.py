from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Validate input to prevent command injection
            if not self.host.replace('.', '').isdigit():
                raise ValueError('Invalid host format')
            output = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': f'Ping command executed with exit code: {output.returncode}
Output: {output.stdout}'}}
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