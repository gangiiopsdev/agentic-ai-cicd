from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Safe execution without shell=True
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

def safe_ping(host: str):
    if not host.strip().isdigit():  # Simplistic validation, improve based on requirements
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        command = PingCommand(host)
        status = command.execute()
        return {"status": status}
    except ValueError as e:
        return {"error": str(e)}