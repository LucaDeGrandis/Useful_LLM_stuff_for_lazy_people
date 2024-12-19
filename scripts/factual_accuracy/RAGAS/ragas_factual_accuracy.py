import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description="A simple script to demonstrate argument parsing.")

    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="A huggingface model."
    )
    parser.add_argument(
        "--api_key",
        type=str,
        required=True,
        help="The huggingface api key."
    )
    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="The path to the dataset."
    )
    parser.add_argument(
        "--sources",
        type=str,
        required=True,
        help="The path to the sources."
    )

    args = parser.parse_args()

    return args


def main():
    pass


if __name__ == "__main__":
    main()
