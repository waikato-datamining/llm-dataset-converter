import argparse
import logging
import traceback

from ldc.core import HUGGINGFACE_DOWNLOAD
from huggingface_hub import hf_hub_download, snapshot_download
from huggingface_hub.constants import REPO_TYPES


_logger = logging.getLogger(HUGGINGFACE_DOWNLOAD)


def download(repo_id: str, repo_type: str = None, filename: str = None, revision: str = None,
             output_dir: str = None, verbose: bool = False):
    """
    Downloads the specified dataset to the output directory.

    :param repo_id: the ID of the repository/dataset to download
    :type repo_id: str
    :param repo_type: the type of the repository, see REPO_TYPES
    :type repo_type: str
    :param filename: when only to download a specific file rather than the whole dataset
    :type filename: str
    :param revision: the revision of the dataset, None for latest
    :type revision: str
    :param output_dir: the directory to store the data in, None for default huggingface cache dir
    :type output_dir: str
    :param verbose: whether to be more verbose
    :type verbose: bool
    """
    if verbose:
        print("Repository ID: %s" % repo_id)
        if repo_type is not None:
            print("Repository type: %s" % repo_type)
        if filename is not None:
            print("Filename: %s" % filename)
        print("Revision: %s" % ("latest" if (revision is None) else revision))
        print("Output: %s" % ("default cache dir" if (output_dir is None) else output_dir))

    if filename is None:
        path = snapshot_download(repo_id, revision=revision, local_dir=output_dir, repo_type=repo_type, local_dir_use_symlinks=False)
    else:
        path = hf_hub_download(repo_id, filename=filename, revision=revision, local_dir=output_dir, repo_type=repo_type, local_dir_use_symlinks=False)
    print("Downloaded: %s" % path)


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description="Tool for downloading files or datasets from huggingface for local conversion.",
        prog=HUGGINGFACE_DOWNLOAD,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--repo_id", help="The name of the huggingface repository/dataset to download", required=True)
    parser.add_argument("-t", "--repo_type", help="The type of the repository", choices=REPO_TYPES, default=None, required=False)
    parser.add_argument("-f", "--filename", help="The name of the file to download rather than the full dataset", default=None, required=False)
    parser.add_argument("-r", "--revision", help="The revision of the dataset to download, omit for latest", default=None, required=False)
    parser.add_argument("-o", "--output_dir", help="The directory to store the data in, stores it in the default huggingface cache directory when omitted.", default=None, required=False)
    parser.add_argument("-v", "--verbose", action="store_true", help="Whether to be more verbose with the output")
    parsed = parser.parse_args(args=args)
    download(parsed.repo_id, repo_type=parsed.repo_type, filename=parsed.filename, revision=parsed.revision,
             output_dir=parsed.output_dir, verbose=parsed.verbose)


def sys_main() -> int:
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    """
    try:
        main()
        return 0
    except Exception:
        print(traceback.format_exc())
        return 1


if __name__ == '__main__':
    main()