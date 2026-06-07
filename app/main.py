from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    return {'status': 'completed', 'result': result}