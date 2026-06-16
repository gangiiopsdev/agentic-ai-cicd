from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        try:
            result = subprocess.run(command, check=True, *args, **kwargs)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    result = SafeSubprocess.safe_call(command)
    return {'status': 'completed', 'result': result}