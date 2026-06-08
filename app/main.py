from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_check_output(cmd, *args, **kwargs):
        for arg in cmd:
            if isinstance(arg, str) and '&&' in arg or ';' in arg:
                raise ValueError('Unsafe command detected')
        return subprocess.check_output(cmd, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = SafeSubprocess.safe_check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}