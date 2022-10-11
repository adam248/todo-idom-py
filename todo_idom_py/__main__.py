from idom import component, html, run


@component
def Item(i: dict, done=False):
    return html.li(i['text'], " ✔" if done else "", key=i['id'])

@component
def DataList(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = list(sorted(items, key=lambda x: x["priority"]))
    list_item_elements = [Item(i) for i in items]
    return html.ul(list_item_elements)

@component
def TodoList():
    tasks = [
        {"id": 0, "text": "Make breakfasts", "priority": 0},
        {"id": 1, "text": "Feed the dog", "priority": 0},
        {"id": 2, "text": "Do laundry", "priority": 2},
        {"id": 3, "text": "Go on a run", "priority": 1},
        {"id": 4, "text": "Clean the house", "priority": 2},
        {"id": 5, "text": "Go to the grocery store", "priority": 2},
        {"id": 6, "text": "Do some coding", "priority": 1},
        {"id": 7, "text": "Read a book", "priority": 1},
        ]

    return html.section(
        html.h1("My Todo List"),
        DataList(tasks, filter_by_priority=1, sort_by_priority=True)
    )

image = html.img({
    "src": "https://picsum.photos/id/237/500/300",
    "style": {"width": "50%", "marginLeft": "25%"},
    "alt": "Billie Holiday",
})

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

@component
def Layout():
    return html.div(
        TodoList(), 
        image,
        Gallery()
        )


run(Layout)
