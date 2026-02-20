tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
"""

insert_tasks = """
INSERT INTO tasks (task) VALUES (?)
"""

read_tasks = """
SELECT id, task, completed FROM tasks
"""

update_tasks = """
UPDATE tasks SET task = ? WHERE id = ?
"""

delete_tasks = """
DELETE FROM tasks WHERE id = ?
"""

update_completed = """
UPDATE tasks SET completed = ? WHERE id = ?
"""