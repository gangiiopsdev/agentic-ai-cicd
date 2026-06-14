from fastapi import FastAPI
import subprocess
generators = {
    "ping": (lambda host: ['ping', host]),
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/{command}')
def command_handler(command, host=None):
    handler = generators.get(command)
    if not handler:
        raise HTTPException(status_code=400, detail=f'Invalid command: {command}')
    args = handler(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}