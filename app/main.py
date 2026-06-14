from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = ['ping'] + shlex.split(host)
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}

app = FastAPI()

def ping_endpoint(host: str):
    return SafePing.ping(host)