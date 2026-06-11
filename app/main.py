from fastapi import FastAPI
import subprocess
import shlex

class SanitizedPing:
    def __call__(self, host: str) -> bool:
        if not self.is_valid_hostname(host):
            return False
        return True

    def is_valid_hostname(self, hostname: str) -> bool:
        return all(c.isalnum() or c in '-.' for c in hostname)

def execute_ping(hostname: str) -> bool:
    try:
        subprocess.run(['ping', shlex.quote(hostname)], check=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

app = FastAPI()
sanitized_ping = SanitizedPing()

@app.get('/ping')
def ping(host: str):
    if not sanitized_ping(host):
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    if execute_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Ping failed'}