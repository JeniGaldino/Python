""""
def file_read_from_line(fname, nlines):
        from itertools import islice
        with open(fname, encoding="utf-8") as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_line('texto.txt',1)
"""
def read_file(fname, nline):
    with open(fname, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if i > nline:
                break
            print(line.strip()) 
            
read_file("dados/namex.txt",2)
