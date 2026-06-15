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

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host input is a valid IP address or hostname before passing it to subprocess.run
    import re
    if not re.match(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$', host) and not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    return PingCommand.execute(host)