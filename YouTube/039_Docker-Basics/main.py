import os, sqlite3
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = os.getenv("DB_PATH", "/data/app.db")  

app = FastAPI(title="Minimal Todo CRUD", description="Beginner-friendly, zero frontend.")

class TodoIn(BaseModel):
    title: str
    completed: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoOut(TodoIn):
    id: int

def row_to_todo(row) -> TodoOut:
    return TodoOut(id=row["id"], title=row["title"], completed=bool(row["completed"]))

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit(); conn.close()

@app.post("/todos", response_model=TodoOut, status_code=201)
def create_todo(payload: TodoIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO todos(title, completed) VALUES(?, ?)",
        (payload.title, int(payload.completed))
    )
    conn.commit()
    row = conn.execute("SELECT * FROM todos WHERE id=?", (cur.lastrowid,)).fetchone()
    conn.close()
    return row_to_todo(row)

@app.get("/todos", response_model=List[TodoOut])
def list_todos():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    conn.close()
    return [row_to_todo(r) for r in rows]

@app.get("/todos/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    conn = get_conn()
    row = conn.execute("SELECT * FROM todos WHERE id=?", (todo_id,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(404, "Todo not found")
    return row_to_todo(row)

@app.patch("/todos/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, payload: TodoUpdate):
    data = payload.model_dump(exclude_unset=True)
    if not data:
        return get_todo(todo_id)  # nothing to change

    fields, values = [], []
    if "title" in data:
        fields.append("title=?"); values.append(data["title"])
    if "completed" in data:
        fields.append("completed=?"); values.append(int(data["completed"]))
    if not fields:
        return get_todo(todo_id)

    conn = get_conn()
    cur = conn.execute(f"UPDATE todos SET {', '.join(fields)} WHERE id=?", (*values, todo_id))
    if cur.rowcount == 0:
        conn.close(); raise HTTPException(404, "Todo not found")
    conn.commit()
    row = conn.execute("SELECT * FROM todos WHERE id=?", (todo_id,)).fetchone()
    conn.close()
    return row_to_todo(row)

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    conn.commit(); conn.close()
    if cur.rowcount == 0:
        raise HTTPException(404, "Todo not found")
    return  # 204 No Content
