# Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love Python.\n"
contents += "I love JavaScript.\n"
contents += "I enjoy playing PlayStation games.\n"
contents += " I love Pizza.\n"
contents += ".I Love watching movies\n"
contents += "I enjoy going to the Gym.\n"


path = Path(
    '/Users/ruan.vanniekerk/Desktop/Code College/VSCode/Python/Chapter10/my_file.txt')
path.write_text(contents)
