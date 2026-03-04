# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    generator_expression_by_major = (student for student in student_list if major.lower() == student[2].lower())
    return generator_expression_by_major