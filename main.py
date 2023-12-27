from datetime import datetime
from blog_parsers.blog_parser_1 import parse_blog_1
from blog_parsers.blog_parser_2 import parse_blog_2
from my_utils.upload import upload
from my_utils.get_category import get_tistory_categories


TODAY = datetime.today().date()
DIFF_DAYS = 14


def main():
    #parse_blog_1(TODAY,DIFF_DAYS)
    #parse_blog_2(TODAY,DIFF_DAYS)

    #upload()
    get_tistory_categories()

if __name__ == "__main__":
    main()