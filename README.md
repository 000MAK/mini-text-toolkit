# Mini Text Toolkit

A lightweight Python command-line utility that reports line, word, and character counts and can normalize whitespace into a separate output file.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## Features

- Counts lines, whitespace-separated words, and Unicode characters.
- Computes a normalized text version using Python's whitespace splitting and joining.
- Prints the summary to the terminal.
- Optionally writes normalized text to a new destination file.
- Rejects identical input and output paths and refuses to overwrite an existing destination.

## Quick start

Analyze a text file:

```bash
python main.py notes.txt
```

Analyze and write a normalized copy:

```bash
python main.py notes.txt --normalize-to normalized.txt
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Scope and limitations

Normalization collapses runs of whitespace, including line breaks, into single spaces. The output is therefore a single normalized text line rather than a preservation of the original paragraph layout. Keep the source file and review the normalized version before using it.

## Related Quantix projects

- [Mini Duplicate Line Finder](https://github.com/000MAK/mini-duplicate-line-finder)
- [Mini CSV Cleaner](https://github.com/000MAK/mini-csv-cleaner)
- [Quantix — 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)

## Safety

Use synthetic examples in public demonstrations; do not commit private notes or customer data.

## License

MIT. See [LICENSE](LICENSE).
