#!/usr/bin/env python3

import psycopg2

sql_most_articles = "SELECT articles.slug, count(*) as Counts FROM log JOIN articles ON CONCAT('/article/', articles.slug) = log.path GROUP BY articles.slug ORDER BY Counts desc LIMIT 5;"
sql_most_author = "SELECT authors.name, count(*) as Counts FROM log JOIN articles ON CONCAT('/article/', articles.slug) = log.path JOIN authors ON authors.id = articles.author GROUP BY authors.name ORDER BY Counts desc;"
sql_errors = "SELECT time::timestamp::date as date, (((SELECT count(*) FROM log WHERE log.time = time::timestamp::date) * 100.0 ) / count(*)) AS Counter FROM log WHERE NOT status = '200 OK' GROUP BY date ORDER BY Counter LIMIT 1;"

try:
        conn = psycopg2.connect("dbname=news")
except:
        print ('Unable to connect to the database')

# Execute SQL query
def execute(query):
    cur = conn.cursor()
    cur.execute(query)
    r = cur.fetchall()
    cur.close()
    return r

# Print a array with count like 1, 2, 3
def most(query, key):
    result = execute(query)
    for i in range(len(result)):
        obj = result[i]
        title = obj[0]
        gets = obj[1]
        print('#', (i + 1), ' | ' + title, ' -> ', gets, key)

# Execute the custom Query and print it in custom format
def moreErrors():
    result = execute(sql_errors)
    r = result[0]
    date = r[0]
    time = r[1]
    print ('>', date, 'which it was', '%s%%' % str(time)[0: 3])

print("Q1: What are the most popular three articles of all time?")
most(sql_most_articles, 'views')
print()
print("----------------------------")
print()
print("Q2: Who are the most popular article authors of all time?")
most(sql_most_author, 'views')
print()
print("----------------------------")
print()
print('Q3: On which days did more than %s%% of requests lead to errors?' % '1')
moreErrors()
conn.close()  # Close the SQL Connection
