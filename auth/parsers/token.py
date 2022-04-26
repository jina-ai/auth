from argparse import ArgumentParser


def set_token_parser(parent_parser: 'ArgumentParser' = None):
    if not parent_parser:
        raise RuntimeError('Unreachable')

    from auth.parsers.helper import _chf

    token_parser = parent_parser.add_subparsers(
        dest='operation',
        required=True,
    )

    create_parser = token_parser.add_parser(
        'create',
        description='Create a Personal Access Token',
        formatter_class=_chf,
    )

    create_parser.add_argument(
        '-e',
        '--expire',
        type=int,
        default=7,
        help='Validity period (days)',
    )

    create_parser.add_argument(
        'name',
        type=str,
        help='Name of Personal Access Token',
    )

    delete_parser = token_parser.add_parser(
        'delete',
        description='Delete a Personal Access Token',
        formatter_class=_chf,
    )

    delete_parser.add_argument(
        'name',
        type=str,
        help='Name of Personal Access Token which you want to delete',
    )
