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
    ping_command = PingCommand(host)
    return ping_command.execute()

# Preventive Controls
# 1. Input Validation: Validate and sanitize the input to ensure it does not contain malicious commands.
# 2. Least Privilege Principle: Run the application with a limited set of permissions.
# 3. Secure Defaults: Configure subprocess to run with the smallest possible privileges.