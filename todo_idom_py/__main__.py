from idom import component, html, run

from .components import TodoApp


@component
def Layout():
    return html.div(
        TodoApp(),
        html.script({"src": "https://unpkg.com/ionicons@5.4.0/dist/ionicons.js"}),
    )


run(Layout)
print("Test")
