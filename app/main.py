from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def execute(host):
        # Enhanced validation and use of shlex.quote for security
        if not host or ' ' in host or '&' in host or ';' in host or '>' in host or '<' in host:
            return "Invalid host"
        subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    if 'Invalid host' in result:
        return {"error": "Invalid host"}, 400
    return {"status": "completed"}