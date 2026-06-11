from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_call(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Failed to ping {host}: {e.output}"

class DependencyContainer:
    def __init__(self):
        self.safe_ping = SafePing()

app = FastAPI()
dependency_container = DependencyContainer()

@app.get("/ping")
def ping(host: str, dependency=Depends(dependency_container)):
    return dependency.safe_call(host)