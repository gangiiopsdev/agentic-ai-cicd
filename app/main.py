from fastapi import FastAPI
import subprocess
class SafeCommand:
    def __init__(self, *args):
        self.args = args

    def execute(self):
        try:
            output = subprocess.run(self.args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_command = SafeCommand('ping', host)
    return safe_command.execute()