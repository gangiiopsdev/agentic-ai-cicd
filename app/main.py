from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            command = ['ping', '-c', '1'] + shlex.split(host)
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output}

app = FastAPI()

def ping(host: str):
    return SafePing.safe_ping(host)