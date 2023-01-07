# Write a Java proaram to convert minutes into a number of
# years and days.
# Test Data
#Input the number of minutes: 3456789
# Expected utout
# 3456789 minutes is approxmately 6 years and 210 days

time = 3456789
# vears = 525600
# davs = 1449

years = time // 525600

left_over_time = time % 525600
days = left_over_time // 1440

print("3456789 minutes is", str(years)+ "years" + str(days) + "days")