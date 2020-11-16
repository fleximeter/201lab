"""
Name: proj1.py
Author: Jeff Martin
Date: 11/16/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a solution for project 1
"""

def mean(values):
    """
    Gets the mean of a set of numbers
    :param values: A list of integers or floats
    :return: The mean (as a float)
    """
    total = 0
    for item in values:
        total += item
    return total / len(values)

def median(values):
    """
    Gets the median of a set of numbers with length > 1
    :param values: A list of integers or floats
    :return: The median
    """
    if len(values) > 1:
        values_copy = list(values)
        values_copy.sort()
        if len(values) % 2 == 1:
            return values_copy[len(values) // 2]
        else:
            median_values = []
            median_values.append(values_copy[len(values) // 2 - 1])
            median_values.append(values_copy[len(values) // 2])
            return mean(median_values)
    else:
        return 0

def stdev(values):
    """
    Gets the standard deviation of a set of numbers
    :param values: A list of integers or floats
    :return: The standard deviation
    """
    mean_value = mean(values)
    temp_values = []
    for i in range(len(values)):
        temp_values.append((values[i] - mean_value) ** 2)
    return mean(temp_values) ** (1/2)

def read_file(filename):
    """
    Reads a text file. Discards first two lines and returns the remaining
    data.
    :param filename: The file to read
    :return: The remaining file data as a single string
    """
    file_data = ""
    with open(filename) as data_file:
        data_file.readline()
        data_file.readline()
        file_data = data_file.read()
    return file_data.strip()

def create_lists(file_contents):
    """
    Reads file data and creates two lists of project scores and exam scores.
    :param file_contents: The file contents to process
    :return: Two lists - one with project scores and one with exam scores
    """
    # create 2d list
    lines = file_contents.split('\n')
    data = []
    proj_list = []
    exam_list = []
    for line in lines:
        data.append(line.split('\t'))

    for i in range(len(data)):
        proj_sum = 0
        exam_sum = 0
        for j in range(2, len(data[i])):
            if j < 5:
                proj_sum += float(data[i][j])
            else:
                exam_sum += float(data[i][j])
        proj_list.append(proj_sum)
        exam_list.append(exam_sum)

    return proj_list, exam_list


def calc_values(project_list, exam_list):
    """
    Calculates mean, median, and stdev from a project list and exam list
    :param project_list: The list of project scores
    :param exam_list: The list of exam scores
    :return: A concatenated string with results
    """
    results_list = []
    results_list.append(str(mean(project_list)))
    results_list.append(str(median(project_list)))
    results_list.append(str(stdev(project_list)))
    results_list.append(str(mean(exam_list)))
    results_list.append(str(median(exam_list)))
    results_list.append(str(stdev(exam_list)))
    return '\t'.join(results_list)


def write_file(list):
    """
    Writes a list of strings to a file
    :param list: The list of strings to write
    :return: nothing
    """
    with open("results.txt", 'a') as results_file:
        for line in list:
            results_file.write(line)

def process_file(filename):
    """
    Performs operations to calculate mean, median, and stdev
    and output data to a file
    :param filename: The file to open
    :return: nothing
    """
    proj_list, exam_list = create_lists(read_file(filename))
    write_file([filename + '\n'])
    write_file(calc_values(proj_list, exam_list) + '\n')

if __name__ == "__main__":
    write_file(["Project Mean\tProject Median\tProject Stdev\t" +
                "Exam Mean\tExam Median\tExam Stdev\n"])
    process_file("fall_2020.txt")
    process_file("spring_2021.txt")
    process_file("fall_2021.txt")
    process_file("spring_2022.txt")