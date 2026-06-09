from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        # Validate the host input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return all(char.isalnum() or char in ['.', '-', '_'] for char in host)

@app.get("/ping")
def ping(host: str):
    try:
        output = PingCommand.run(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}