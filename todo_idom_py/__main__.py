from idom import component, html, run

from .gallery import Gallery, ScrollingGallery
from .playpause import PlayPauseApp
from .todo import TodoList


@component
def Layout():
    return html.div(
        ScrollingGallery(),
        PlayPauseApp(),
        TodoList(), 
        )


run(Layout)
