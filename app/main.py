from fastapi import FastAPI
import subprocess
import shlex

class FastAPI:
    def __init__(self):
        self.routes = []

    def get(self, path: str):
        def decorator(func):
            self.routes.append((path, func))
            return func
        return decorator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation with additional validation and escaping
    if not host or ' ' in host:
        raise ValueError("Invalid input")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}