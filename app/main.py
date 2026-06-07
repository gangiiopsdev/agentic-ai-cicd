from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Safe implementation using subprocess.run()
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Vulnerable implementation removed
    output = ping_command.execute(host)
    return {"status": "completed", "output": output}