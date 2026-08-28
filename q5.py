import pandas as pd
df = pd.read_csv("data/student_performance.csv")
print(df.head())
row,column=df.shape
print("no of row:",row,"and no of column:",column)
print("column names:",df.columns)
for x in df.isnull().sum():
    if x!=0:
        print("there are datasets missing values")
else:
    print("there are no datasets missing values")
print("the mean valuue of final score is:",df["Final_Score"].mean())
val=df["Final_Score"].max()
for x in range(0,len(df)):
    if df.loc[x,"Final_Score"]==val:
        print("student with highest score:",df.loc[x,"Student"],"with mark :",val)

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
l=[]
for x in range(0,len(df)):
    if df.loc[x,"Attendance"]>=80:
        l.append(df.loc[x,"Student"])
        
print("students with attendance greater than or equal to 80 is:",l)
df = df.sort_values(by="Final_Score", ascending=False)
df.to_csv("processed_student_performance.csv", index=False)

