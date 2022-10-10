from todo_idom_py import __version__


def test_version():
    """Compares the version number in pyproject.toml and the __init__.py file in the main project directory.
    You will need to `poetry add -D toml`"""
    from pathlib import Path

    import toml
    
    pyproject = Path("./pyproject.toml")
    pyproject = toml.load(pyproject)
    assert __version__ == pyproject["tool"]["poetry"]["version"]
