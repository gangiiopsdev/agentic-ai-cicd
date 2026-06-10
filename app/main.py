from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        # Validate the host to ensure it does not contain any shell metacharacters or malicious code
        if self.is_valid_host(self.host):
            return subprocess.call(command)
        else:
            raise ValueError('Invalid host provided')

    def is_valid_host(self, host):
        import re
        # Regex to validate the host (simple example, adjust as needed)
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        result = ping_command.execute()
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}