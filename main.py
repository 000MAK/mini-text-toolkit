import argparse
from pathlib import Path

def analyze(text):
    normalized=" ".join(text.split())
    return {"lines":len(text.splitlines()),"words":len(text.split()),"characters":len(text),"normalized":normalized}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("--normalize-to"); a=ap.parse_args(); text=Path(a.input).read_text(encoding="utf-8-sig"); r=analyze(text)
    print(f"Lines: {r['lines']}\nWords: {r['words']}\nCharacters: {r['characters']}\nNormalized: {r['normalized']}")
    if a.normalize_to:
        dst=Path(a.normalize_to)
        if dst.resolve()==Path(a.input).resolve(): ap.error("Output must differ from input")
        if dst.exists(): ap.error("Output already exists; choose a new path")
        dst.write_text(r["normalized"]+"\n",encoding="utf-8")
if __name__=="__main__": main()
