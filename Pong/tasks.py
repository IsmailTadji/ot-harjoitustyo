from invoke import task

@task
def start(ctx):
    ctx.run("python3 logic/Pong.py", pty = True)