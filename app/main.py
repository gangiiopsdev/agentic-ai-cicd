from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    async def execute(self, host: str):
        # Safer implementation
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

global_ping_command = PingCommand()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = global_ping_command.execute(host)
    return {"status": "completed", "result": result}