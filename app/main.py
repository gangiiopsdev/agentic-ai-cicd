from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Validate and sanitize the host input
            if not self.host or not isinstance(self.host, str) or not self.host.strip():
                raise ValueError('Invalid host')
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in (',', '.', '-', '_'))
    command = PingCommand(sanitized_host)
    output = command.execute()
    return {"status": "completed", "output": output}