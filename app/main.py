from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    def __init__(self, cmd: str, *args, **kwargs):
        self.cmd = cmd
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = subprocess.run([self.cmd] + list(map(subprocess.Popen.quote, self.args)), check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_subprocess = SafeSubprocess('ping', host)
    return safe_subprocess.run()