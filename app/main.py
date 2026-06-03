from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize user input to prevent command injection
        if not host.replace('.', '').isnumeric() or len(host.split('.')) != 4:
            raise ValueError('Invalid IP address')
        ping_command = PingCommand(host)
        result = ping_command.execute()
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}