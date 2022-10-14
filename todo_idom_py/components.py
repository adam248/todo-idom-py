import dataclasses
import json

from idom import component, html, use_state

from .datastructure import TodoList


def event_dbg(event):
    print(json.dumps(event, indent=4))


@component
def Button(label, color=None, on_click=event_dbg, visible=True):

    return html.button(
        {
            "class": "btn",
            "onClick": on_click,
            "style": {
                "backgroundColor": color,
                "borderRadius": "8px",
                "margin-left": "0.5em",
                "visibility": "hidden" if not visible else "visible",
            },
        },
        label,
    )


@component
def Item(i: dict, tasks, set_tasks):
    editing, set_editing = use_state(False)
    visible, set_visible = use_state(False)

    def on_checkbox(event):
        i["done"] = not i["done"]
        set_tasks(tasks)

    def on_edit(event):
        if editing:
            set_editing(False)
        else:
            set_editing(True)

    def on_edit_input_changed(event):
        i["text"] = event["target"]["value"]
        set_tasks(tasks)

    def on_key_press(event):
        if event["keyCode"] == 13:
            on_edit(event)

    def on_delete(event):
        set_tasks([t for t in tasks if t["id"] != i["id"]])

    display = html.label(
        {
            "style": {
                "margin": "0.5em",
                "textDecoration": "line-through" if i["done"] else "",
            }
        },
        i["text"],
    )
    if editing:
        display = html.input(
            {
                "text": i["text"],
                "onChange": on_edit_input_changed,
                "onKeyPress": on_key_press,
            }
        )

    return html.li(
        {
            "onMouseOver": lambda e: set_visible(True),
            "onMouseLeave": lambda e: set_visible(False),
        },
        html.input(
            {
                "onChange": on_checkbox,
                "type": "checkbox",
                "value": i["id"],
                "checked": i["done"],
            }
        ),
        display,
        Button("✏️", color="blue", on_click=on_edit, visible=visible),
        Button("🗑️", color="red", on_click=on_delete, visible=visible),
        key=i["id"],
    )


@component
def NewTask(tasks, set_tasks):
    task_text, set_task_text = use_state("")

    def on_add(event):
        if task_text != "":
            set_task_text("")
            print(f"Add new task {task_text}")
            set_tasks([*tasks, TodoList.add_task(task_text)])

    def on_change(event):
        set_task_text(event["target"]["value"])

    return html.div(
        {"style": {"margin": "0.5em"}},
        html.span(
            html.input({"onChange": on_change, "value": task_text}),
            Button("➕", color="green", on_click=on_add),
        ),
    )


@component
def DataList(tasks, set_tasks, filter_by_priority=None, sort_by_priority=False):
    if filter_by_priority:
        tasks = [i for i in tasks if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        tasks = list(sorted(tasks, key=lambda x: x["priority"]))
    list_item_elements = [Item(i, tasks, set_tasks) for i in tasks]
    return html.ul(
        {
            "style": {"listStyleType": "none"},
        },
        NewTask(tasks, set_tasks),
        list_item_elements,
    )


@component
def TodoApp():
    t = TodoList()

    tasks, set_tasks = use_state(t.tasks)

    return html.section(
        {"style": {"margin": "0.5em"}},
        html.h1("My Todo List"),
        DataList(tasks, set_tasks, filter_by_priority=1, sort_by_priority=True),
    )
