from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Validate and sanitize the host input
            if not self.host or 'ping' in self.host.lower():
                raise ValueError('Invalid host parameter')

            # Use a whitelist of allowed hosts
            allowed_hosts = ['google.com', 'example.com']  # Example list, should be dynamic and secure
            if self.host not in allowed_hosts:
                raise ValueError('Host not allowed')

            # Sanitize the host input using shlex.quote to handle special characters safely
            sanitized_host = shlex.quote(self.host)

            result = await subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()