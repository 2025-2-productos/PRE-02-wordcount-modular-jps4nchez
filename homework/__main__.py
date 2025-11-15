import argparse

from .src.wordcount import main


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Word count pipeline")
    parser.add_argument("input_dir", help="Directory containing the input text files")
    parser.add_argument("output_dir", help="Directory where the TSV will be saved")
    return parser.parse_args()


def run_cli() -> None:
    args = parse_args()
    main(args.input_dir, args.output_dir)


if __name__ == "__main__":
    run_cli()
