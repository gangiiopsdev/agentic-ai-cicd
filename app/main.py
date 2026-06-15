from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(f'{{}}'.format(part.replace('{', '{{}').replace('}', '{{}}')) for part in arg.split())

@app.get="/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', escape_shell_arg(host)])

    return {'status': 'completed'}