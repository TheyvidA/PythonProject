import pandas as pd

# Displays the results of the surveys
Survey = pd.read_csv('stack-overflow-developer-survey-2024/survey_results_public.csv', index_col='ResponseId')
pd.set_option('display.max_columns', 114)
pd.set_option('display.max_rows', 114)
print(Survey)

# Displays the questions of the survey
Schema_df = pd.read_csv('stack-overflow-developer-survey-2024/survey_results_schema.csv', index_col='qname')
print(Schema_df)

# Displays the top 5 results of the Question
print(Schema_df.head(5))
print(Schema_df.tail(5))

# Displays the top 5 results of the Survey
print(Survey.head(5))
print(Survey.tail(5))

# Displays all the columns in each csv files
print(Survey.columns)
print(Schema_df.columns)

# Displays the
#d1 = Survey.loc['Employment']
print(d1)

d1 = Survey['Employment']
print(d1.value_counts())

# Displays the question of the Organization size
d2 = Schema_df.loc['OrgSize', 'question']
print(d2)

# Sorting the Questions
print(Schema_df.sort_index())

# Displays people with Salary of over $60,000
#High_salary = (Survey['CompTotal'] > 60000)
#H1 = Survey.loc[High_salary, ['Country', 'LanguageWantToWorkWith', 'CompTotal']]
print(H1)

# Filtering by selected countries(USA,UK,India,Germany,Canada and Nigeria) with > $60,000 salary
#Countries = ['United States of America', 'United Kingdom of Great Britain and Northern Ireland', 'Germany', 'India', 'Nigeria', 'Canada']
#filt = (Survey['Country'].isin(Countries) & High_salary)
#filt2 = Survey.loc[filt]
print(filt2)

# Renaming of Some columns
Rename = Survey.rename(columns={'MainBranch':'Profession', 'RemoteWork':'WorkMode', 'CompTotal':'SalaryUSD'}, inplace=True)
print(Survey['SalaryUSD'])

# Sorting the Country and Salary column in Survey Data
#Survey.sort_values(by=[['Country', 'SalaryUSD']], ascending=[True, False], inplace=True)
print(Survey[['Country', 'SalaryUSD']].head(7))

# Displays the 10 highest Salary per Annum
print(Survey['ConvertedCompYearly'].nlargest(10))
print(Survey.nlargest(10, 'ConvertedCompYearly'))

# Displays the 10 lowest Salary per Annum
print(Survey['ConvertedCompYearly'].nsmallest(10))
print(Survey.nsmallest(10, 'ConvertedCompYearly'))

# Displays the industries people chose in the Survey
print(Survey['Industry'].value_counts())

# Using the groupby function to check the people who took the survey from Nigeria
country_grp = Survey.groupby(['Country'])
print(country_grp.get_group('Nigeria'))

# Displays the industries of those who took the survey based on their Countries
print(country_grp['Industry'].value_counts())

# Displays the industries of Nigerians who took the Survey
filt = Survey['Country'] == 'Nigeria'
print(Survey.loc[filt]['Industry'].value_counts())

# Displays the Percentage of Indians,Russia and China who took the Survey based on their Industries
print(country_grp['Industry'].value_counts(normalize=True).loc[['India', 'Russian Federation', 'China']])

# Displays the Means/Median/Min/Max of the annual salary of those who took the survey based on their countries
print(country_grp['ConvertedCompYearly'].agg(['mean', 'median', 'min', 'max']))

# Displays people who have worked with Python prog lang according to their countries
Python_PerCountry = country_grp['LanguageHaveWorkedWith'].apply(lambda X: X.str.contains('Python').sum())
print(Python_PerCountry)

# Displays the percentage of respondents who have worked with Python per country
Country_respondents = Survey['Country'].value_counts()
print(Country_respondents)

CountryPythonUsed = country_grp['LanguageHaveWorkedWith'].apply(lambda X: X.str.contains('Python').sum())
print(CountryPythonUsed)

PythonPerRespondents = pd.concat([Country_respondents, CountryPythonUsed], axis='columns')
print(PythonPerRespondents)

PythonPerRespondents['PctPython'] = (PythonPerRespondents['LanguageHaveWorkedWith']/PythonPerRespondents['count']) * 100
print(PythonPerRespondents)

PythonPerRespondents.sort_values(by='PctPython', ascending=False, inplace=True)
print(PythonPerRespondents.head(30))
