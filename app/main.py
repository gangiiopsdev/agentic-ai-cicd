from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            # Validate input to prevent command injection
            if not self.is_valid_host(self.host):
                return {'status': 'failed', 'error': 'Invalid host'}
            result = await subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    def is_valid_host(self, host):
        # Add validation logic here
        return all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.run()