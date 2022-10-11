from idom import component, html


@component
def PrintButton(display, message):
    def handle_event(event):
        print(message)
    
    return html.button({"onClick": handle_event}, display)

@component
def PlayPauseApp():
    return html.div(
        PrintButton("Play", "Playing"),
        PrintButton("Pause", "Paused"),
    )
