from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def is_valid_host(self, host: str) -> bool:
        return all(char in self.valid_chars for char in host)

    def run_command(self, args: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(args, capture_output=True, text=True)

class PingService(SafePing):
    def ping_host(self, host: str) -> dict:
        if not self.is_valid_host(host):
            raise ValueError('Invalid host name')
        args = ['ping', host]
        result = self.run_command(args)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    output = ping_service.ping_host(host)
    return output