
from datetime import datetime, timedelta
from blog_parsers.blog_parser_1 import parse_blog_1


TODAY = datetime.today().date()
DIFF_DAYS = 14

def main():
    parse_blog_1(TODAY,DIFF_DAYS)

if __name__ == "__main__":
    main()