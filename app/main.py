from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def safe_command(command_parts):
        return subprocess.Popen(shlex.split(' '.join(command_parts)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    try:
        result = SafeCommand.safe_command(command_parts)
        output, error = result.communicate()
        if error:
            raise Exception(f'Error pinging {host}: {error.decode()}')
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'message': str(e)}