import argparse


def set_base_parser():
    from .. import __version__
    from .helper import _chf, colored

    parser = argparse.ArgumentParser(
        description=f'Jina auth (v{colored(__version__, "green")}) helps you login in to Jina Ecosystem.',
        formatter_class=_chf,
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__,
        help='Show version',
    )
    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'CRITICAL', 'NOTSET'],
        default='INFO',
        help='Set the loglevel of the logger',
    )
    return parser