contents = ["this is string one",
            "this is string two",
            "this is string 3"]

filenames = ["string_one.txt", "string_two.txt", "string_three.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
