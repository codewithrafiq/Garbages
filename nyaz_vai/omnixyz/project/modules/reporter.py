import re
from project import config, BASE_DIR

def generate_report():
    # define and open file
    filename = BASE_DIR / config.file.file_name

    counter_integer = 0
    counter_float = 0
    counter_alphanumeric = 0
    counter_alphabetic = 0


    # File Read
    f = open(filename, "r")
    txt = f.read()
    splitted_txt = re.split("\,", txt)
    # print(splitted_txt)


    for item in splitted_txt:
        item = item.strip()
        try:
            if isinstance(eval(str(item)), int):
                counter_integer+=1
            elif isinstance(eval(str(item)), float):
                counter_float+=1
        except:
            if (item.isalpha()):
                counter_alphabetic+=1
            else:
                counter_alphanumeric+=1
        
    print({'integer': counter_integer, 'float': counter_float, 'alphanumeric': counter_alphanumeric, 'alphabetic': counter_alphabetic})
    data = {'integer': counter_integer, 'float': counter_float, 'alphanumeric': counter_alphanumeric, 'alphabetic': counter_alphabetic}
    return data



