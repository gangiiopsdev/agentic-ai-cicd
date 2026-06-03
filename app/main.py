from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingCommand.safe_ping(host)
    return {'status': 'completed', 'result': result}