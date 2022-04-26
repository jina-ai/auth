import hubble


def login(args):
    hubble.login()


def logout(args):
    hubble.logout()


def token(args):
    client = None
    try:
        client = hubble.Client(max_retries=None, timeout=10)
    except Exception as e:
        if isinstance(e, ValueError):
            print('🚨 Please login first')
            return

    if args.operation == 'create':
        response = client.create_personal_access_token(
            name=args.name, expiration_days=args.expire
        )

        response.raise_for_status()
        token = response.json()['data']['token']

        import rich
        from rich.panel import Panel

        rich.print(
            Panel(
                f'token: [b]{token}[/b]',
                title=':party_popper: [green]Successfully created',
                subtitle=':point_up:️ [red]Please keep this token in a safe place!',
                width=50,
            )
        )

    if args.operation == 'delete':
        response = client.delete_personal_access_token(
            personal_access_token_id=args.name
        )

        response.raise_for_status()

        import rich
        from rich.panel import Panel

        rich.print(
            Panel(
                f'[b]{args.name}[/b]',
                title=':party_popper: [green]Successfully deleted',
                width=50,
            )
        )

    if args.operation == 'list':
        response = client.list_personal_access_tokens()
        response.raise_for_status()
        tokens = response.json()['data']['personal_access_tokens']

        import rich
        from rich.table import Table

        table = Table(title="Your personal access tokens")
        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Type", style="magenta")
        table.add_column("Name", justify="center", style="green")
        table.add_column("ExpireAt", justify="center", style="green")
        table.add_column("CreatedAt", justify="center", style="green")
        table.add_column("UpdatedAt", justify="center", style="green")

        for token in tokens:
            table.add_row(
                token['_id'],
                token['type'],
                token['name'],
                token['expireAt'],
                token['createdAt'],
                token['updatedAt'],
            )

        rich.print(table)
