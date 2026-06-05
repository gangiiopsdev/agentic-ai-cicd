from fastapi import FastAPI
import subprocess
class CommandRunner:
    def run(self, host):
        # Validate host input
        if not self.is_valid_host(host):
            return "Invalid host"
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

    def is_valid_host(self, host):
        # Add validation logic here, e.g., check if the host is a valid IP address or hostname
        import re
        pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
        return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner()
    output = runner.run(host)
    return {"status": "completed", "output": output}