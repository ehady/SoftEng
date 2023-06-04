import pandas as pd

studentPerformance = pd.read_csv("C:\\Users\\lenovo\\Downloads\\StudentsPerformance.csv")

mean_math = studentPerformance['math score'].mean()
mean_reading = studentPerformance['reading score'].mean()
mean_writing = studentPerformance['writing score'].mean()

means = []
means.append(mean_writing)
means.append(mean_reading)
means.append(mean_math)

greatest = max(means)

missing_values = studentPerformance.isnull().sum()

for column, count in missing_values.items():
    if count > 1:
        studentPerformance = studentPerformance.dropna(subset=[f'{column}'])

median = studentPerformance['math score'].median()
SP_bachelor = studentPerformance[(studentPerformance['parental level of education'] == "bachelor's degree") & (studentPerformance['math score'] > median)]

SP_female = len(studentPerformance[studentPerformance['gender'] == 'female'])
SP_male = len(studentPerformance[studentPerformance['gender'] == 'male'])

total = len(studentPerformance)

ratio_female = SP_female / total
ratio_male = SP_male / total

races = studentPerformance['race/ethnicity']

group = races.value_counts()
print(group)
print(group.nunique() == 1)