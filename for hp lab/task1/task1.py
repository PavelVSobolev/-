
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name1', nargs='?')
    parser.add_argument ('name2', nargs='?')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    n = int(namespace.name1)
    m = int(namespace.name2)

    path = ""
    fn = 1
    while True:
        path += str(fn)
        fn = 1 + (fn - 2 + m) % n
        if fn == 1:
            break
    print(path)


