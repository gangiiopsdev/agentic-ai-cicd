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

app = FastAPI()
sanitized_ping = SanitizedPing()

@app.get('/ping')
def ping(host: str):
    if not sanitized_ping(host):
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    subprocess.run(['ping', shlex.quote(host)], check=True, text=True)
    return {'status': 'completed'}