from fastapi import FastAPI
import subprocess
import shlex
class Ping:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        # Safe implementation
        args = ['ping', host]
        subprocess.call(args)

if __name__ == "__main__":
    Ping()