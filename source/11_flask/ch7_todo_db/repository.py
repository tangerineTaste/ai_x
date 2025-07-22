import pymysql
conn = pymysql.connect(host='localhost', user='root', password='mysql', database='devdb')

from models import TodoRequest
from typing import List

def get_todos(order) -> List[dict]:
    cursor = conn.cursor()
    if order == 'asc':
        sql = 'SELECT * FROM TODO ORDER BY ID ASC'
    else:
        sql = 'SELECT * FROM TODO ORDER BY ID DESC'
    cursor.execute(sql)
    keys = [desc[0] for desc in cursor.description]
    todos = [dict(zip(keys, desc)) for desc in cursor.fetchall()]
    cursor.close()
    return todos

def get_next_id() -> int:
    cursor = conn.cursor()
    sql = 'SELECT IFNULL(MAX(ID), 0)+1 FROM TODO'
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0] # type: ignore

def get_todo(id: int) -> dict:
    cursor = conn.cursor()
    sql = 'SELECT * FROM TODO WHERE ID = %s'
    cursor.execute(sql, (id))
    result = cursor.fetchone()
    cursor.close()
    return {'id': result[0], 'content': result[1], 'is_done': result[2]} # type: ignore

def create_todo(todo: TodoRequest) -> None:
    cursor = conn.cursor()
    sql = 'INSERT INTO TODO VALUES (%s, %s, %s)'
    cursor.execute(sql, (todo.id, todo.content, todo.is_done))
    conn.commit()
    cursor.close()
    return cursor.rowcount # type: ignore

def update_todo(todo: TodoRequest) -> str:
    cursor = conn.cursor()
    sql = 'UPDATE TODO SET CONTENTS = %s, IS_DONE = %s WHERE ID = %s'
    cursor.execute(sql, (todo.content, todo.is_done, todo.id))
    conn.commit()
    cursor.close()
    if cursor.rowcount:
        return f'{todo.id}번 {todo.content}을 수정.'
    return f'{todo.id}번 할일을 찾을 수 없습니다.'

def delete_todo(id: int) -> str:
    cursor = conn.cursor()
    sql = 'DELETE FROM TODO WHERE ID = %s'
    cursor.execute(sql, (id))
    conn.commit()
    cursor.close()
    if cursor.rowcount:
        return f'{id}번 삭제.'
    return f'{id}번을 찾을 수 없습니다.'

if __name__ == '__main__':
    todos = get_todos('asc')
    print(todos)
    max = get_next_id()
    print(max)
    todo = get_todo(1)
    print(todo)
    #print(create_todo(TodoRequest(id=get_next_id(), contents='새로운 할일', is_done=False)))
    #print(update_todo(TodoRequest(id=1, content='수정된 할일', is_done=True)))
    #print(delete_todo(1))
