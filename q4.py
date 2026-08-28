import numpy as np
hours=np.array([2,5,6,8,4])
attendance=np.array([80,92,85,98,88])
previous=np.array([60,75,68,90,72])
final=np.array([70,91,58,87,76])
print("shape of array hours is:",hours.shape,"and data type is:",hours.dtype)
print("shape of array attendance is:",attendance.shape,"and data type is:",attendance.dtype)
print("shape of array previous is:",previous.shape,"and data type is:",previous.dtype)
print("shape of array final is:",final.shape,"and data type is:",final.dtype)
print("the mean final score is:",final.mean())
print("the minimum and maximum final score is:",final.max(),final.min(),sep=" ")
print("the standard deviation of final score:",final.std())
bonus=final+5
print("bonus five added to final score:",bonus)
passed=final>=75
print("the boolean array of those who have scored atleast 75:",passed)
name=np.array(["nikhil","ashish","pranav","guna","senthil"])
print("students who scored atleast 75:",name[passed])
print("scores grreater than or equal to 75:",final[passed])
