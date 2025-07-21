import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# employee_data = pd.read_sql("""SELECT * FROM employees;""", conn)
# print(employee_data)


# print(pd.read_sql("""
# SELECT *
#   FROM employees;
# """, conn))

# employees_first_and_last = pd.read_sql("""
# SELECT lastName, firstName
#   FROM employees;
# """, conn).head()

# print(employees_first_and_last)


# employees_first_and_last = pd.read_sql("""
# SELECT firstName, lastName
#   FROM employees;
# """, conn).head()

# print(employees_first_and_last)


# employees_first_names = pd.read_sql("""
# SELECT firstName AS name
#   FROM employees;
# """, conn).head()

# print(employees_first_names)


# employees_by_role = pd.read_sql("""
# SELECT firstName, lastName, jobTitle,
#        CASE
#        WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
#        ELSE "Not Sales Rep"
#        END AS role
#   FROM employees;
# """, conn).head(10)

# print(employees_by_role)


# employees_with_location = pd.read_sql("""
# SELECT firstName, lastName, officeCode,
#        CASE
#        WHEN officeCode = "1" THEN "San Francisco, CA"
#        WHEN officeCode = "2" THEN "Boston, MA"
#        WHEN officeCode = "3" THEN "New York, NY"
#        WHEN officeCode = "4" THEN "Paris, France"
#        WHEN officeCode = "5" THEN "Tokyo, Japan"
#        END AS office
#   FROM employees;
# """, conn).head(10)

# print(employees_with_location)


employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
       CASE officeCode
       WHEN "1" THEN "San Francisco, CA"
       WHEN "2" THEN "Boston, MA"
       WHEN "3" THEN "New York, NY"
       WHEN "4" THEN "Paris, France"
       WHEN "5" THEN "Tokyo, Japan"
       END AS office
  FROM employees;
""", conn).head(10)

print(employees_with_location)

conn.close()