from fastapi import FastAPI
import subprocess
import shlex

class SanitizedPing:
    def __init__(self, host: str):
        if not self._is_valid_host(host):
            raise ValueError('Invalid host input')
        self.host = shlex.quote(host)

    @staticmethod
def _is_valid_host(host: str) -> bool:
        return all(c.isalnum() or c == '.' for c in host) and '.' in host

app = FastAPI()

@app.get("/ping")
def ping(sanitized_host: SanitizedPing):
    args = ['ping', sanitized_host.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}