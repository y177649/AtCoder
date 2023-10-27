for i in range(34, 325):
    filename = f"a{i}.py"
    with open(filename, 'w') as file:
        file.write(f"# This is file {i}\n")