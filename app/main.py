from fastapi import FastAPI
import subprocess
import shlex

class FastAPISubprocess:
    def __init__(self):
        self.app = FastAPI()

    def ping(self, host: str):
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in '._-')
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}

# Usage
if __name__ == '__main__':
    app_instance = FastAPISubprocess()
    app_instance.app.mount('/', app_instance.ping)