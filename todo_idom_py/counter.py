from idom import component, html, use_state

counter = 0

@component
def Counter():
    number, set_number = use_state(counter)

    def handle_click(event):
        global counter
        counter += 1
        set_number(counter)

    return html.div(
        html.h1(number),
        html.button({"onClick": handle_click}, "Count"),
    )

