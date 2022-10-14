import json

from idom import component, html, use_state

from .datastructure import TodoList


def event_dbg(event):
    print(json.dumps(event, indent=2))


@component
def Button(label, color=None, on_click=event_dbg):

    return html.button(
        {
            "class": "btn",
            "onClick": on_click,
            "style": {
                "backgroundColor": color,
                "borderRadius": "8px",
            },
        },
        label,
    )


@component
def Item(i: dict):
    def on_checkbox(event):
        key = i["id"]
        print(f"Toggled checkbox: {key}")

    def on_edit(event):
        key = i["id"]
        print(f"Edit: {key}")

    def on_delete(event):
        key = i["id"]
        print(f"Delete: {key}")

    return html.li(
        html.input({"onChange": on_checkbox, "type": "checkbox"}),
        html.label({"style": {"margin": "0.5em"}}, i["text"]),
        Button("✏️", color="blue", on_click=on_edit),
        Button("🗑️", color="red", on_click=on_delete),
        key=i["id"],
    )


@component
def NewTask():
    def on_add(event):
        print("Add new task")

    return html.span(
        html.input({"onChange": event_dbg}),
        Button("➕", color="green", on_click=on_add),
    )


@component
def DataList(items, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = list(sorted(items, key=lambda x: x["priority"]))
    list_item_elements = [Item(i) for i in items]
    return html.ul(
        {
            "style": {"listStyleType": "none"},
        },
        NewTask(),
        list_item_elements,
    )


@component
def TodoApp():
    t = TodoList()

    return html.section(
        {"style": {"margin": "0.5em"}},
        html.h1("My Todo List"),
        DataList(t.tasks, filter_by_priority=1, sort_by_priority=True),
    )
