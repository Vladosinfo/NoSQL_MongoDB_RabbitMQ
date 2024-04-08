from db.models import Author, Quotes
from db.db_connect import db_connect


def name(name):
    authors = Author.objects(fullname__istartswith = name)

    res = []
    for author_item in authors:
        # auth = author_item.to_mongo().to_dict()
        # print(auth)
        quotes = Quotes.objects(author = author_item)

        if quotes:
            for q in quotes:
                # res[author_item.fullname] = [q.quote for q in quotes]
                adict = {
                    'author':q.author.fullname,
                    'born_date':q.author.born_date,
                    'born_location':q.author.born_location,
                    'quote':q.quote,
                    'tags':q.tags
                }
                res.append(adict)

    return res

        
def tag(tag):
    # quotes = Quotes.objects(tags__in=['life', 'humor'])
    quotes = Quotes.objects(tags__istartswith=tag)
    # tag = Quotes.objects(tags__eq=tag)
    # quotes = Quotes.objects(tags__contains=tag)
    for quote in quotes:
        print(quote.quote)

def tags(tags):
    pass

def parse_string(str):
    ar_str = str.split(":")
    return command_handler(ar_str)

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
    db_connect()
    while True:
        user_input = input("Input command >>> ")
        user_input = user_input.strip().lower()
        if user_input == "exit":
            break
        res = parse_string(user_input)
        print(res)


if __name__ == "__main__":
    main()
