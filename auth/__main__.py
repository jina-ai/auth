def main():
    from .pasers import get_main_parser

    args = get_main_parser().parse_args()
    
    print(args)

if __name__ == '__main__':
    main()