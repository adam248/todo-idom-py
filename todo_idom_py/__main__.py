from idom import component, html, run

from .components import TodoApp


@component
def Layout():
    return html.div(
        TodoApp(),
    )


run(Layout)
print("Test")
