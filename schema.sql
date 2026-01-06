CREATE TABLE users (user_id TEXT PRIMARY KEY, name TEXT, email TEXT, role TEXT);
CREATE TABLE teams (team_id TEXT PRIMARY KEY, name TEXT);
CREATE TABLE projects (project_id TEXT PRIMARY KEY, team_id TEXT, name TEXT, type TEXT);
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY, 
    project_id TEXT, 
    assignee_id TEXT, 
    title TEXT, 
    notes TEXT, 
    status TEXT, 
    created_at TIMESTAMP
);