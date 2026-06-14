from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        try:
            # Further sanitize the host input to prevent command injection
            sanitized_host = ''.join(c for c in host if c.isalnum() or c in ('.', ':', '/'))
            output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return PingCommand.execute(host)