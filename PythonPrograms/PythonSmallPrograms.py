# 1. BMI calculator

age = 30
weight = 78
height = 1.67
bmi = weight / (height * 2)
print(type(bmi))
print(f"Your BMI is {int(bmi)}")
if bmi < 25:
    print("you are under weight")
elif 25 >= bmi >= 50:
    print("You are normal")
else:
    print("You are over weight")

# 2. No of weeks left Calculator

age = input("what is your age")
age_in_weeks = int(age) * 52
age_in_days = int(age) * 52 * 365

print(type(age_in_weeks))
print(f" my age in is {age}, in weeks would be {age_in_weeks}, and in days would be {age_in_days}")

age_90 = 90 * 52
year_90 = 90
days_90 = 90 * 52 * 365

years_left = year_90 - int(age)
weeks_left = age_90 - age_in_weeks
days_left = days_90 - age_in_days

print(f"You have {days_left} days,{weeks_left} weeks,and {years_left} years left")
