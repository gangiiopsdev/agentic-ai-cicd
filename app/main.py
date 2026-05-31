from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.strip().isdigit():
        raise ValueError("Invalid host input")
    return host
class PingCommand:
    def __init__(self, host):
        self.host = validate_host(host)
    def run(self):
        # Sanitize the host input to prevent command injection
        sanitized_host = subprocess.list2cmdline([self.host])
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
        return {"status": "completed", "output": result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str): 
    try:
        command = PingCommand(host)
        return command.run()
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}