from fastapi import FastAPI
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}