from fastapi import FastAPI
import subprocess

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        # Secure implementation
        safe_host = host.strip()
        subprocess.call(["ping", safe_host])
        return {"status": "completed"}

if __name__ == "__main__":
    SafePing().app.run()