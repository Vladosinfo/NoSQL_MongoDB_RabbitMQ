from db.models import Author, Quotes
from db.db_connect import db_connect

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--tag", type=str, help="command for inpyt tag/tags")
# parser.add_argument("--name", type=str, help="command for inpyt name of quote")
# args = parser.parse_args()


def form_dict(quotes):
    res = []

    for q in quotes:
        dict = {
            'author':q.author.fullname,
            'born_date':q.author.born_date,
            'born_location':q.author.born_location,
            'quote':q.quote,    # [1:-1]
            'tags':q.tags
        }
        res.append(dict)

    return res


@cache
def name(name):
    authors = Author.objects(fullname__istartswith = name)

    res = []
    for author_item in authors:
        # auth = author_item.to_mongo().to_dict()
        quotes = Quotes.objects(author = author_item)

        if quotes:
            res.extend(form_dict(quotes))

    return res

        
@cache        
def tag(tag):
    res = []
    quotes = Quotes.objects(tags__istartswith=tag)
    if quotes:
        res.extend(form_dict(quotes))

    return res


def tags(tags):
    tags = tags.split(",")
    res = []
    for tag_item in tags:
        tag_result = tag(tag_item)
        if len(res) < 1:
            res = tag_result
        else:
            item_exists = 0
            for item_res in res:
                for item_tag_result in tag_result:
                    if item_res['quote'] == item_tag_result['quote']:
                        item_exists = 1
                        break
                if item_exists == 1:
                    break
            if item_exists == 0:
                res.extend(tag_result)

    return res
        

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


def print_result(list):
    print('-'*75)
    for item in list:
        for key, val in item.items():
            print(f"{key}: {val}")
        print('-'*75)


def main():
    # print(args.action)
    db_connect()
    while True:
        user_input = input("Input command >>> ")
        user_input = user_input.strip().lower()
        if user_input == "exit":
            break
        res = parse_string(user_input)
        print_result(res)


if __name__ == "__main__":
    main()
