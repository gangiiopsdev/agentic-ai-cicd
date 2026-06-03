from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' in host:
        command = ["ping", host]
        for arg in command:
            if not arg.isalnum() and not any(char.isdigit() or char.isalpha() for char in arg):
                raise ValueError('Invalid argument')
        subprocess.run(command, check=True)
    else:
        raise ValueError('Invalid command')
    return {"status": "completed"}