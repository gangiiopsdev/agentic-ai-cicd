from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host):
        if self.is_valid_host(host):
            ping_command = ['ping', '-c', '1'] + [shlex.quote(host)]
            return subprocess.run(ping_command, capture_output=True, text=True)
        else:
            raise ValueError("Invalid host")

    def is_valid_host(self, host):
        # More comprehensive validation to ensure the input does not contain shell metacharacters
        import re
        return re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}