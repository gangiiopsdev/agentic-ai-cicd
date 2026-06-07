from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}
    command = PingCommand(host)
    return command.execute()

# Apply additional controls:
# 1. Use a whitelist of allowed hosts.
# 2. Limit the duration of the subprocess to prevent denial of service attacks.
# 3. Log all subprocess executions for auditing and forensic analysis.