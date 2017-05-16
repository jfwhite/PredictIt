#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import json
from bs4 import BeautifulSoup
import requests
import base64
import numpy as np
import math

# Connect to database
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Prepare useful constants
STEM = ["MAT", "PHY", "MOL", "EEB", "CBE", "ELE", "COS", "CHM", "MAE", "AST", "CEE", "ORF", "SML"] 
HUM = ["POR", "LAT", "CLA", "HUM", "ENG", "HIS", "PHI", "MUS", "SLA", "COM", "AAS", "SPA", "PER"]
offerings_url = "https://registrar.princeton.edu/course-offerings/"
eval_url = "https://reg-captiva.princeton.edu/chart/index.php?courseinfo="
term = "1182"

# Load departmental averages
f = open("deptavgs.txt")
deptavgs = {}
for line in f:
    (dept, avg) = line.split()
    if avg != "-1":
        deptavgs[dept] = float(avg)
m = np.mean(deptavgs.values())
f = open("deptavgs.txt")
for line in f:
    (dept, avg) = line.split()
    if float(avg) < 0:
        deptavgs[dept] = m

# Process JSON to add a course to coursedata table
def insert_course(cid, code, name):
    if cid in ids:
        return # don't duplicate courses, violating PRIMARY KEY constraint
    dim1 = int(code[3:6]) # course level 
    dim2 = get_dim2(code) # course STEM-ness, currently sketchy
    dim3 = get_dim3(cid) # course enrollment
    name = code
    rating = get_rating(cid, code[0:3])
    statement = "INSERT INTO coursedata VALUES ('{id}', {d1}, {d2}, {d3}, '{name}', '{rating}')"
    print name
    c.execute(statement.format(id=cid, d1=dim1, d2=dim2, d3=dim3, name=name, rating=rating))
    ids.append(cid) # add to list of "visited" courseids
    conn.commit()

# Lookup the course rating - do I use Selenium or Base64? interpolation will be hard too
def get_rating(cid, dept):
    r = requests.get(eval_url+cid)
    b = BeautifulSoup(r.text, "lxml")
    input = b.find_all("input")
    ratings = [deptavgs[dept]]
    if input:
        koolchart = json.loads(base64.b64decode(input[1].attrs["value"]))
        ratings = [float(item["YValue"]) for item in koolchart["PlotArea"]["ListOfSeries"][0]["Items"]]
    return round(np.mean(ratings), 3)

# Extract the course STEM-ness
def get_dim2(course):
    if course[0:3] in STEM:
       return 30 # very STEM
    elif course[0:3] in HUM:
       return 10 # very non-STEM
    else:
       return 20 # in between: social sciences and other

def get_dim3(course):
    r = requests.get(offerings_url+"course_details.xml?term="+term+"&courseid="+course)
    s = BeautifulSoup(r.text, "lxml")
    e = s.find(text="Enrolled:").parent.next_sibling.strip() # broken for multiple section-classes
    return int(e)

# Initialize list of "visited" courseids
c.execute("SELECT CIDS FROM COURSEDATA")
ids = [row[0] for row in c.fetchall()]

# Get all courseids
r = requests.get(offerings_url+"search_results.xml?term="+term)
s = BeautifulSoup(r.text, "lxml")
for a in s.find_all("a"):
    h = a.get("href", "not found")
    if "course_details.xml" in h:
        coursecode = " ".join(a.text.split()[0:2])
        name = a.parent.next_sibling.next_sibling.text.strip()
        insert_course(h[28:34], coursecode, name)

# Or iterate through all possible - maybe try both?

# Close database connection
conn.commit()
conn.close()
