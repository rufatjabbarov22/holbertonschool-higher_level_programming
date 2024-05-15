import uncompyle6

def decompile_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        source_code = uncompyle6.decompile_file(None, f)
    return source_code

def extract_names(source_code):
    names = []
    exec(source_code, globals(), locals())
    for name, value in locals().items():
        if not name.startswith('__'):
            names.append(name)
    return names

if __name__ == "__main__":
    pyc_file = "hidden_4.pyc"
    source_code = decompile_pyc(pyc_file)
    names = extract_names(source_code)
    for name in names:
        print(name)
