from idom import component, html, use_state


@component
def Counter():
    number, set_number = use_state(0)

    def handle_click(event):
        set_number(number + 1)

    return html.div(
        html.h1(number),
        html.button({"onClick": handle_click}, "Count"),
    )

