from fastapi import FastAPI
import subprocess
import shlex
import os

class SanitizedPing:
    def __call__(self, host: str) -> bool:
        if not self.is_valid_hostname(host):
            return False
        return True

    def is_valid_hostname(self, hostname: str) -> bool:
        return all(c.isalnum() or c in '-.' for c in hostname)

app = FastAPI()
sanitized_ping = SanitizedPing()

def safe_execute(command: list) -> None:
    if os.name == 'posix':
        subprocess.run(command, check=True, text=True)
    else:
        # Handle Windows separately or remove if not needed
        pass

@app.get('/ping')
def ping(host: str):
    if not sanitized_ping(host):
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    safe_execute(['ping', shlex.quote(host)])  # Ensure host is properly quoted to prevent injection
    return {'status': 'completed'}