filesnames = ["1.doc", "1.report", "1.presentation"]

new_filenames = [filename.replace('.','-') + '.txt' for filename in filesnames]

print(new_filenames)