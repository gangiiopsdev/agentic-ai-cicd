from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingCommand.run(host)
    return {'status': 'completed', 'result': result}