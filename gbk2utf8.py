from sys import argv

def gbk_to_utf8(source, target):
    with open(source, "r", encoding="gb2312") as src:
        with open(target, "w", encoding="utf-8") as dst:
            for line in src.readlines():
                dst.write(line)
        dst.close()

if __name__ == '__main__':
    source = argv[1]
    target = argv[2]
    gbk_to_utf8(source,target)

