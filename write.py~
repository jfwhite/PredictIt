import sqlite3
import json

conn = sqlite3.connect("courses.db")
c = conn.cursor()

f = open("courses.json")
j = json.load(f)
STEM = ["MAT", "PHY", "MOL", "EEB", "CBE", "ELE", "COS", "CHM", "MAE", "AST", "CEE", "ORF", "SML"] 
HUM = ["POR", "LAT", "CLA", "HUM", "ENG", "HIS", "PHI", "MUS", "SLA", "COM", "AAS", "SPA", "PER"]
term = "1182"

def get_dim1(course):
    if course.get("listings"):
        return course.get("listings")[0]["number"]
    else:
        return -1

def get_dim2(course):
    if course.get("listings"):
        if course.get("listings")[0]["dept"] in STEM:
            return 30
        elif course.get("listings")[0]["dept"] in HUM:
            return 10
        else:
            return 20
    else:
        return -1

def get_dim3(course):
    if course.get("classes"):
        return course["classes"][0]["enroll"]
    else:
        return -1

def insert_course(course):
    cid = course["courseid"]
    if cid in ids:
        return
    dim1 = get_dim1(course)
    dim2 = get_dim2(course)
    dim3 = get_dim3(course)
    statement = "INSERT INTO coursedata VALUES ('{id}', {d1}, {d2}, {d3})"
    c.execute(statement.format(id = cid, d1 = dim1, d2 = dim2, d3 = dim3))
    ids.append(cid)

c.execute("SELECT ID FROM COURSEDATA")
ids = [row[0] for row in c.fetchall()]

for course in j:
    insert_course(course)

conn.commit()
conn.close()
