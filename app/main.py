from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_subprocess(command: list):
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode())

app = FastAPI()

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    command = shlex.split(f'ping {host}')
    result = SafeSubprocess.safe_subprocess(command)
    return {'status': 'completed', 'result': result}