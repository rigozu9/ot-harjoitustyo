"""invoke import"""
from invoke import task

@task
def start(ctx):
    """starting the program"""
    ctx.run("python src/index.py", pty=True)

@task
def test (ctx):
    """running the tests"""
    ctx.run("pytest src", pty=True)

@task
def coverage_report(ctx):
    """running the coverage tests and getting the html report"""
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    """run lint"""
    ctx.run("pylint src", pty=True)