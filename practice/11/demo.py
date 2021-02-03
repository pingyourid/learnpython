# from name_function import get_full_name

# str = get_full_name('zhang', 'bin')
# print(str)

#---

from survey import Survey

question = '\nWhat is your favorite color?'
survey = Survey(question)

while True:    
    result = input(f"{question} Enter 'q' to quit\n")
    if result == 'q':
        break
    else:
        survey.insert_response(result)


survey.report()
