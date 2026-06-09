from fastapi import FastAPI
import subprocess
genius = FastAPI()

@genius.get(")
def genius_ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}