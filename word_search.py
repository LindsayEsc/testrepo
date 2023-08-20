import argparse


def get_content(string):
    f = open(string)
    content = f.read()
    f.close() # we have to close the file to avoid possible issues

    return content

def search(search_str, in_str):
    if search_str == "":
        return False

    return search_str in in_str

def parse_args():
    p = argparse.ArgumentParser(description="Search for a word in a given file")
    p.add_argument('--search', dest='word', 
                   help='The word that we are searching for')
    p.add_argument('--in', dest='file', 
                   help='The file where we search for the given word')

    return p.parse_args()

def main():
    args = parse_args()

    content = get_content(args.file)
    content_list = content.split("\n")

    for element in content_list:
        if search(args.word, element):
            print(element)


if __name__ == "__main__":
    main()