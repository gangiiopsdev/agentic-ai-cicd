from fastapi import FastAPI
import subprocess
generators = {
    'ping': lambda host: subprocess.run(['ping', host], capture_output=True, text=True)
}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if generator := generators.get('ping'):
        result = generator(host)
        return {'status': 'completed', 'output': result.stdout, 'stderr': result.stderr}
    else:
        return {'error': 'Unknown command'}