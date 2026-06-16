from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def is_valid_host(self, host: str) -> bool:
        return all(c in self.valid_chars for c in host)

    def run_command(self, command: list) -> dict:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def safe_ping(self, host: str) -> dict:
        if not self.is_valid_host(host):
            raise ValueError('Invalid host name')
        command = ['ping', host]
        return self.run_command(command)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):\n    return safe_ping_instance.safe_ping(host)