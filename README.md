# CSV-to-Nested-JSON-Python
A simple Python code to convert CSV files to nested JSON objects. Quite handy when you have to load CSV or Excel file into Document DB like MONGO DB, Azure COSMOS DB etc..

In the given example, it takes the input CSV file and groups the data based on the following columns:
JobID,JobDate,JobTitle,Division,State

Multiple Skills exists for the job and they are created as nested JSON.
The following columns appear in the nested JSON. 

DetailedSkill,SkillGroup,SkillMasterGroup


Sample Input File:

Sample1.csv

Output:

Jobs.json
