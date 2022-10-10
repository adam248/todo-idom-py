from idom import component, html, run


@component
def HelloWorld():
    return html.div(
    html.h1("My Todo List"),
    html.ul(
        html.li("Design a cool new app"),
        html.li("Build it"),
        html.li("Share it with the world!"),
    )
)

run(HelloWorld)
