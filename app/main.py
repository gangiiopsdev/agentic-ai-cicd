from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Safe implementation using subprocess.run with validation
        if not host.strip().replace('.', '').isnumeric():
            raise ValueError('Invalid host name or IP address')
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), result.stderr.decode()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, error = PingCommand.execute(host)
    return {"output": output, "error": error}