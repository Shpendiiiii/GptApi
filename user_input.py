def give_prompt():
    dict = {}
    user_input = input("Enter your prompt: ")
    file_extension = input("Want to convert into a specifc file format (press enter to skip): ")
    dict["prompt"] = user_input
    if file_extension == "":
        return dict
    dict["extension"] = file_extension
    return dict
