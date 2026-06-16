from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Validate the host to ensure it only contains allowed characters and does not start or end with a dot
        safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
        if safe_host.startswith('.') or safe_host.endswith('.'):  # Prevents potential command injection
            raise ValueError('Invalid hostname')
        try:
            result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f'Ping command failed with error {e.__str__()}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    return {"status": "completed", "output": result}