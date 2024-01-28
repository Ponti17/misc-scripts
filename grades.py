import csv

def calculate_weighted_average(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        weight_sum = 0
        total_points = 0
        for row in reader:
            grade = int(row['Grade'])
            ects = int(row['ECTS'])
            weight = ects / 5
            weight_sum += weight
            total_points += grade * weight
        return total_points / weight_sum

# Replace 'your_file.csv' with the actual filename of your CSV file
csv_file_path = 'grades.csv'
average_grade = calculate_weighted_average(csv_file_path)

print(f"The weighted average grade is: " + str(average_grade))
