from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host):
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    response = SafePing.safe_ping(host)
    return {'status': 'completed', 'response': response}