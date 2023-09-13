#!/usr/bin/python3
""" The Append After Module"""


def append_after(filename="", search_string="", new_string=""):
	""" To Search and Update """
	read = []
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
        index = 0

        while index < len(read):
			if search_string in read[index]:
				read[index:index + 1] = [read[index], new_string]
				index += 1
            index += 1

	with open(filename,"w",encoding="utf-8") as file:
		file.writelines(read)
