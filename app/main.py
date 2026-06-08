from fastapi import FastAPI
import shlex
class SafePing:
    def __call__(self, host: str):
        # Validate the host input to ensure it only contains allowed characters
        if not self.is_valid_host(host):
            return False, 'Invalid host'
        cmd = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout,

    def is_valid_host(self, host: str) -> bool:
        # Implement a simple regex to validate the host format
        import re
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    status, output = safe_ping(host)
    return {"status": status, "output": output}