import glob
import sys
from pathlib import Path
def search_content(content):
    
    """
    Returns a list with all the .txt files inside the data directory that have the given string
    """
    
    files_to_search = glob.glob("data/*.txt")
    readfile = lambda fp: Path(fp).read_text()
    check = lambda file: content in readfile(file)
    occurrences = sorted(filter(check, files_to_search))
    
    return occurrences


def main():
    printer = lambda p: print("- {0} \n".format(p))
    try:
        print("Arquivos com a string:")
        [printer(f)  for f in search_content(sys.argv[1])]
    except Exception as e:
        print("Error: {0}".format(e))
        print("script usage: python search.py <string_wanted>")
    finally:
        exit()


if __name__ == '__main__':
    main()