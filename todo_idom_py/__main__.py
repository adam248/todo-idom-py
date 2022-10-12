from idom import component, html, run

from .todo import TodoList


@component
def Layout():
    return html.div(
        TodoList(),
    )


run(Layout)
print("Test")
