import sqlite3
from pathlib import Path


SCHEMA = """
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  major TEXT NOT NULL
);
CREATE TABLE enrollments (
  student_id INTEGER NOT NULL,
  course TEXT NOT NULL,
  FOREIGN KEY(student_id) REFERENCES students(id)
);
"""


def demo_db(path: Path | None = None) -> dict:
    uri = ":memory:" if path is None else str(path)
    con = sqlite3.connect(uri)
    con.executescript(SCHEMA)
    con.executemany(
        "INSERT INTO students(id, name, major) VALUES (?,?,?)",
        [(1, "Ada", "ECE"), (2, "Alan", "CSE")],
    )
    con.executemany(
        "INSERT INTO enrollments(student_id, course) VALUES (?,?)",
        [(1, "DSA"), (1, "DBMS"), (2, "ML")],
    )
    rows = con.execute(
        """
        SELECT s.name, COUNT(e.course) AS n
        FROM students s
        JOIN enrollments e ON e.student_id = s.id
        GROUP BY s.name
        ORDER BY s.name
        """
    ).fetchall()
    con.close()
    return {"rows": rows}
