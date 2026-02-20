import flet as ft
from db import main_db

def main(page: ft.Page):

    tasks_column = ft.Column(controls=[])
    def load_tasks():
        tasks_column.controls.clear()
        for task_id, task_text_value, completed in main_db.get_all_tasks():
            row = create_task_row(task_id, task_text_value, completed)
            tasks_column.controls.append(row)
        page.update()
    def create_task_row(task_id, task_text_value, completed):

        def edit_task_text(e):
            main_db.edit_task(task_id, task_text.value)
            task_text.read_only = True
            page.update()

        def delete_task_row(e):
            main_db.delete_task(task_id)
            tasks_column.controls.remove(task_row)
            page.update()

        def toggle_completed(e):
            new_value = 1 if completed_checkbox.value else 0
            main_db.update_task_completed(task_id, new_value)
            task_text.color = "#008000" if completed_checkbox.value else "#000000"
            page.update()

        task_text = ft.TextField(value=task_text_value, expand=True, read_only=True)
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, icon_color="#000000",
                                    on_click=lambda e: setattr(task_text, "read_only", False))
        save_button = ft.IconButton(icon=ft.Icons.SAVE, icon_color="#000000", on_click=edit_task_text)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color="#B71C1C", on_click=delete_task_row)
        completed_checkbox = ft.Checkbox(value=completed == 1, on_change=toggle_completed)
        task_text.color = "#008000" if completed_checkbox.value else "#000000"

        task_row = ft.Row([completed_checkbox, task_text, edit_button, save_button, delete_button])
        return task_row
    def add_new_task(e):
        if user_input.value:
            task_id = main_db.add_new_task(user_input.value)
            row = create_task_row(task_id, user_input.value, 0)
            tasks_column.controls.append(row)
            user_input.value = ""
            page.update()
    user_input = ft.TextField(label="Новая задача", expand=True, on_submit=add_new_task)
    add_button = ft.IconButton(icon=ft.Icons.ADD, icon_color="#000000", on_click=add_new_task)
    input_row = ft.Row([user_input, add_button])

    page.add(input_row, tasks_column)
    
    load_tasks()


if __name__ == "__main__":
    main_db.create_tables()
    ft.app(target=main)