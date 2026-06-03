from fastapi import FastAPI
import subprocess
def run_git_command(command):
    if not is_valid_command(command):
        raise ValueError('Invalid command')
    try:
        result = subprocess.run(command.split(), shell=False, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
def is_valid_command(command):
    # Implement validation logic here
    allowed_commands = ['git pull', 'git push']
    if command in allowed_commands:
        return True
    return False