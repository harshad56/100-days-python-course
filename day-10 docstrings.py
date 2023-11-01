#return an early exit 
def format_name(f_name,l_name):
    """Take  a first and last name and foramt it to return the title case version of the name"""


    if f_name == "" or l_name == "":
        return " write your first and last name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name}{formated_l_name}"

format_name("harshad","bagal")