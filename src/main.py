import sqlite3
import os
from generators.users import build_users
from generators.projects import build_projects

def run_simulation():
    db_file = 'output/asana_simulation.sqlite'
    conn = sqlite3.connect(db_file)
    
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    
    staff = build_users(50)
    for s in staff:
        conn.execute("INSERT INTO users VALUES (?,?,?,?)", (s['id'], s['name'], s['email'], s['role']))
    
    conn.commit()
    conn.close()
    print("Simulation finished. Data saved to asana_simulation.sqlite")

if __name__ == "__main__":
    run_simulation()