from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty = True)

@task
def build(ctx):
    ctx.run("python3 src/initialise_db.py", pty = True)

@task
def test(ctx):
    ctx.run("python -m pytest src/tests/", pty = True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty = True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty = True)

@task
def coverage_report_open(ctx):
    ctx.run("open htmlcov/index.html")

@task
def lint(ctx):
    ctx.run("pylint src", pty = True)

