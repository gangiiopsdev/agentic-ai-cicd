from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = PingCommand.run(host)
    return {"status": "completed", "output": output}