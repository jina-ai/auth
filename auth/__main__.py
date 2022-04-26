def main():
    import os

    from auth.parsers import get_main_parser

    args = get_main_parser().parse_args()

    if args.log_level:
        os.environ['JINA_AUTH_LOG_LEVEL'] = args.log_level

    try:
        # TODO: enable verify latest version after publishing package

        # import threading
        # from .helper import is_latest_version

        # threading.Thread(
        #     target=is_latest_version, daemon=True, args=('jina-auth',)
        # ).start()
        from auth import api

        getattr(api, args.cli.replace('-', '_'))(args)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
