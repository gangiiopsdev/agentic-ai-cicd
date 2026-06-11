from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Safe implementation using subprocess.run without shell=True
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return "Invalid host"
    return PingCommand.execute(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., checking if the host is a valid IP address or hostname
    return True