# CSV-to-Nested-JSON-Python
A simple Python code to convert CSV files to nested JSON objects. Quite handy when you have to load CSV or Excel file into Document DB like MONGO DB, Azure COSMOS DB etc..

In the given example, it takes the input CSV file and groups the data based on the following columns:
JobID,JobDate,JobTitle,Division,State

Multiple Skills exists for the job and they are created as nested JSON.
The following columns appear in the nested JSON. 

DetailedSkill,SkillGroup,SkillMasterGroup


Sample Input File:

JobID,JobDate,JobTitle,Division,State,DetailedSkill,SkillGroup,SkillMasterGroup
525235235,1/01/2018,Auditor,,NSW,Audit Planning,Auditing,Finance
525235235,1/01/2018,Financial Analyst,Financial and Insurance Services,NSW,Credit Analysis,Risk Management,Business
525235235,1/01/2018,Financial Analyst,Financial and Insurance Services,NSW,Business Operations,Business Process and Analysis,Business
521285899,4/01/2018,Auditor,Financial and Insurance Services,NSW,Audit Engagements,Auditing,Finance
521257717,5/01/2018,Auditor,,NSW,Business Operations,Business Process and Analysis,Business
521257717,5/01/2018,Auditor,,NSW,Internal Auditing,Auditing,Finance
521362625,7/01/2018,Management Accountant,,VIC,Account Reconciliation,General Accounting,Finance
521362625,7/01/2018,Management Accountant,,VIC,Accounting,General Accounting,Finance
521362625,7/01/2018,Management Accountant,,VIC,Budgeting,Budget Management,Finance
521362625,7/01/2018,Management Accountant,,VIC,Corporate Finance,Corporate Accounting,Finance
681362625,11/01/2018,Management Accountant,,VIC,Financial Statements,Financial Reporting,Finance



Output:

[{'Division': '',
  'JobDate': '1/01/2018',
  'JobId': '525235235',
  'JobTitle': 'Auditor',
  'Skills': [{'DetailedSkill': 'Audit Planning',
              'SkillGroup': 'Auditing',
              'SkillMasterGroup': 'Finance'}],
  'State': 'NSW'},
 {'Division': 'Financial and Insurance Services',
  'JobDate': '1/01/2018',
  'JobId': '525235235',
  'JobTitle': 'Financial Analyst',
  'Skills': [{'DetailedSkill': 'Credit Analysis',
              'SkillGroup': 'Risk Management',
              'SkillMasterGroup': 'Business'},
             {'DetailedSkill': 'Business Operations',
              'SkillGroup': 'Business Process and Analysis',
              'SkillMasterGroup': 'Business'}],
  'State': 'NSW'},
 {'Division': 'Financial and Insurance Services',
  'JobDate': '4/01/2018',
  'JobId': '521285899',
  'JobTitle': 'Auditor',
  'Skills': [{'DetailedSkill': 'Audit Engagements',
              'SkillGroup': 'Auditing',
              'SkillMasterGroup': 'Finance'}],
  'State': 'NSW'},
 {'Division': '',
  'JobDate': '5/01/2018',
  'JobId': '521257717',
  'JobTitle': 'Auditor',
  'Skills': [{'DetailedSkill': 'Business Operations',
              'SkillGroup': 'Business Process and Analysis',
              'SkillMasterGroup': 'Business'},
             {'DetailedSkill': 'Internal Auditing',
              'SkillGroup': 'Auditing',
              'SkillMasterGroup': 'Finance'}],
  'State': 'NSW'},
 {'Division': '',
  'JobDate': '7/01/2018',
  'JobId': '521362625',
  'JobTitle': 'Management Accountant',
  'Skills': [{'DetailedSkill': 'Account Reconciliation',
              'SkillGroup': 'General Accounting',
              'SkillMasterGroup': 'Finance'},
             {'DetailedSkill': 'Accounting',
              'SkillGroup': 'General Accounting',
              'SkillMasterGroup': 'Finance'},
             {'DetailedSkill': 'Budgeting',
              'SkillGroup': 'Budget Management',
              'SkillMasterGroup': 'Finance'},
             {'DetailedSkill': 'Corporate Finance',
              'SkillGroup': 'Corporate Accounting',
              'SkillMasterGroup': 'Finance'}],
  'State': 'VIC'},
 {'Division': '',
  'JobDate': '11/01/2018',
  'JobId': '681362625',
  'JobTitle': 'Management Accountant',
  'Skills': [{'DetailedSkill': 'Financial Statements',
              'SkillGroup': 'Financial Reporting',
              'SkillMasterGroup': 'Finance'}],
  'State': 'VIC'}]
