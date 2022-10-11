from idom import component, html, run

from .counter import Counter
from .gallery import Gallery, ScrollingGallery
from .playpause import PlayPauseApp
from .todo import TodoList


@component
def Layout():
    return html.div(
        Counter(),
        ScrollingGallery(),
        PlayPauseApp(),
        TodoList(), 
        )


run(Layout)
