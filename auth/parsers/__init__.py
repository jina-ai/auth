def get_main_parser():
    """The main parser for Jina
    :return: the parser
    """
    from .base import set_base_parser
    from .helper import _chf
    from .token import set_token_parser

    # create the top-level parser
    parser = set_base_parser()

    sp = parser.add_subparsers(
        dest='cli',
        required=True,
    )

    sp.add_parser(
        'login',
        description='Login to Jina Ecosystem',
        formatter_class=_chf,
    )

    sp.add_parser(
        'logout',
        description='Logout Jina Ecosystem',
        formatter_class=_chf,
    )

    set_token_parser(
        sp.add_parser(
            'token',
            description='Operations on Personal Access Token',
            formatter_class=_chf,
        )
    )

    return parser
