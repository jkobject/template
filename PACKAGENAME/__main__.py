import argparse


def main():
    """
    main function to preprocess datasets in a given lamindb collection.
    """
    parser = argparse.ArgumentParser(
        description="Preprocess datasets in a given lamindb collection."
    )
    parser.add_argument(
        "--instance",
        type=str,
        default=None,
        help="Instance storing the input dataset, if not local",
    )
    parser.add_argument(
        "--version", type=str, default=None, help="Version of the input dataset."
    )
    parser.add_argument(
        "--filter_gene_by_counts",
        type=int,
        default=0,
        help="Determines whether to filter genes by counts.",
    )
    args = parser.parse_args()

    # do stuff


if __name__ == "__main__":
    main()
