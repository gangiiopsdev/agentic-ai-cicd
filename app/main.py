from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = PingCommand.safe_ping(host)
        if isinstance(result, str) and 'Permission denied' in result:
            return {'status': 'failed', 'error': result}
        else:
            return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}