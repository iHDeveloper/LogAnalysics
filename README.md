# Log Analysics
It's a program that helps you to analyse logs and some other things in database using SQL. It finds which articles is the most popular at all the time. Also, most popular authors at all the time and on which days the errors did more then 1%.
It took the data from **news** database.

# Requirements
- You need to have [Python V3](https://www.python.org/)
- You need to have Virtual Machine like [Virtual Box](https://www.virtualbox.org)
- You need to have [Vagrant](https://www.vagrantup.com/)
- You need to have **news** installed in the your virtual machine [news.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- You need to install `psycopg2`
```
pip install psycopg2
```

# Install the news database
```
psql -d news -f newsdata.zip
```
- If it says database not found then do this
```
createdb news
```
- and then do the same command to implement the database inside the news database.

# How to run
- You may use `python3` but maybe you have it as `python`. It depends on how did you configure it.
```
python main.py
```
# Does it need any views?
No it doesn't need any views it uses the tables that are in the database

# License
It's open source code. Also, It doesn't have any license. You are free to do whatever you want on it.

# Example of Output
You will find an example of the output of the program in `example.txt`