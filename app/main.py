from fastapi import FastAPI
import subprocess

def run_git_command(command):
    if not isinstance(command, str) or not command.strip().startswith('git '):
        raise ValueError("Invalid command")
    return subprocess.run(command, shell=False, capture_output=True, text=True)