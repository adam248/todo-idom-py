from idom import component, html, run

from .counter import Counter
from .gallery import Gallery, ScrollingGallery
from .moving import MovingDot
from .playpause import PlayPauseApp
from .todo import TodoList


@component
def Layout():
    return html.div(
        MovingDot(),
        Counter(),
        ScrollingGallery(),
        PlayPauseApp(),
        TodoList(),
    )


run(Layout)
print("Test")
