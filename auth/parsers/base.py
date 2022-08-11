import argparse


def set_base_parser():
    from auth.parsers.helper import _chf

    parser = argparse.ArgumentParser(
        description=f'Jina auth helps you login in to Jina Ecosystem.',  # noqa F501
        formatter_class=_chf,
    )

    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'CRITICAL', 'NOTSET'],
        default='INFO',
        help='Set the loglevel of the logger',
    )
    return parser
