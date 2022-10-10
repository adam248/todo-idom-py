from idom import component, html, run


@component
def HelloWorld():
    return html.h1("Hello, World!")

run(HelloWorld)
