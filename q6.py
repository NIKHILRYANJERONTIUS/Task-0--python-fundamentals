import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_student_performance.csv")
plt.bar(df["Student"], df["Final_Score"])
plt.title("Student  vs Final Scores")
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.savefig("final_scores.png")
plt.show()
plt.close()


plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.savefig("study_vs_score.png")
plt.show()
plt.close()


plt.hist(df["Final_Score"])
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.show()
plt.close()

'''As attedance increases, the final score also increase is an intersting relationship''''

plt.scatter(df["Attendance"], df["Final_Score"])
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.savefig("custom_plot.png")
plt.show()
plt.close()

