import json
from pathlib import Path

from idom import component, hooks, html


@component
def Photo(alt_text, image_id):
    return html.img({
        "src": f"https://picsum.photos/id/{image_id}/500/200",
        "style": {"width": "50%", "marginLeft": "25%"},
        "alt": alt_text,
    })

@component
def Gallery():
    return html.section(
        html.h1("Photo Gallery"),
        Photo("Landscape", image_id=830),
        Photo("City", image_id=274),
        Photo("Puppy", image_id=237),
    )


def get_data():
    HERE = Path(__file__)
    DATA_PATH = HERE.parent / "data.json"
    return json.loads(DATA_PATH.read_text())


@component
def ScrollingGallery():
    index, set_index = hooks.use_state(0)

    def handle_click(event):
        set_index(index + 1)

    sculpture_data = get_data()
    bounded_index = index % len(sculpture_data)
    sculpture = sculpture_data[bounded_index]
    alt = sculpture["alt"]
    artist = sculpture["artist"]
    description = sculpture["description"]
    name = sculpture["name"]
    url = sculpture["url"]

    return html.div(
        html.button({"onClick": handle_click}, "Next"),
        html.h2(name, " by ", artist),
        html.p(f"({bounded_index + 1} of {len(sculpture_data)})"),
        html.img({"src": url, "alt": alt, "style": {"height": "200px"}}),
        html.p(description),
    )

