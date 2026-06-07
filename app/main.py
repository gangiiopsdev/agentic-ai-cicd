from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_args(args):
    return [arg.replace('`', '\\`').replace('$', '\$') for arg in args]

@app.get="/ping")
def ping(host: str):

    # Secure implementation
    args = ['ping'] + escape_shell_args([host])
    subprocess.call(args)

    return {'status': 'completed'}