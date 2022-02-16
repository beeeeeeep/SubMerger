from argparse import ArgumentParser
import srt
import ass


def parse_args():
    parser = ArgumentParser(description="Merge subs")
    parser.add_argument("-e", "--eng", type=str, help="English subs file", required=True)
    parser.add_argument("-j", "--jpn", type=str, help="Japanese subs file", required=True)

    return parser.parse_args()


args = parse_args()
with open(args.eng, encoding="utf-8") as fp:
    eng = srt.parse(fp.read())

with open(args.jpn, encoding="utf_8") as fp:
    raw = fp.read()
    jpn = ass.parse(raw)

print(len(eng))
print(len(jpn))
