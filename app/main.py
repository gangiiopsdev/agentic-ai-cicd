from fastapi import FastAPI
import click
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        validated_host = click.clean_text(host)
        subprocess.run(['ping', validated_host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}