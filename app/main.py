from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout, None
        except subprocess.CalledProcessError as e:
            return None, str(e.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {"error": "Invalid host parameter"}
    command = PingCommand(host)
    stdout, stderr = command.execute()
    return {
        "status": "completed",
        "stdout": stdout,
        "stderr": stderr
    }