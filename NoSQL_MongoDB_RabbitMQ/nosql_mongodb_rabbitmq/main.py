# from .db.db_connect
from .db.models import Author, Quotes
from .db.db_connect import db_connect
# from .db.db_connect import db_connect


def name(name):
    # notes = Notes.objects(tags__name__in=['Fun', 'Purchases'])
    quotes = Quotes.objects(author__fullname=name)
    for quote in quotes:
        tags = [tags for tag in quote.tags]
        author = [f'fullname: {author.fullname}, born_date: {author.born_date}, born_location: {author.born_location} description: {author.description}' for author in quote.author]
        print(f"id: {quote.id} tags: {tags} author: {author} quote: {quote.quote}") 
        
def tag(arg):
    tag = Quotes.objects(tags='arg')
    print(tag)

def tags(tags):
    pass

def parse_string(str):
    ar_str = str.split(":")
    command_handler(ar_str)

def command_handler(args):
    print(args)
    handler = COMMAND_HANDLER.get(args[0])
    return handler(args[1].strip())


COMMAND_HANDLER = {
    "name": name,
    "tag": tag,
    "tags": tags,
    "exit": exit
}

def main():
    while True:
        user_input = input("Input command >>> ")
        user_input = user_input.strip().lower()
        if user_input == "exit":
            break
        parse_string(user_input)


if __name__ == "__main__":
    main()
