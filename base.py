import requests


class Joker:
    def __init__(self, joke_category):
        self.category = joke_category

    def joker_func(self):
        joker_url = f"https://v2.jokeapi.dev/joke/{self.category}"
        joker_json = requests.get(joker_url).json()

        if 'joke' in joker_json:
            joke_var = joker_json['joke']
            return joke_var

        elif 'setup' in joker_json:
            joke_var = joker_json['setup']
            joke_var2 = joker_json['delivery']
            joke_list = [joke_var, joke_var2]
            return joke_list


def facts():
    facts_url = "https://api.api-ninjas.com/v1/facts?limit=1"
    facts_api = requests.get(facts_url, headers={"X-Api-Key": "API KEY" })
    fact_output = facts_api.json()[0]["fact"]
    return fact_output


def quotes(quote_category):
    quotes_url = f"https://api.api-ninjas.com/v1/quotes?category={quote_category}"  # add category format
    quotes_api = requests.get(quotes_url, headers={"X-Api-Key": "API KEY"})
    a = quotes_api.json()[0]["quote"]
    b = quotes_api.json()[0]["author"]
    return a, b


def bucket_list():
    bucket_url = "https://api.api-ninjas.com/v1/bucketlist"
    bucket_api = requests.get(bucket_url, headers={"X-Api-Key": "API KEY"})

    bucket_list_item = bucket_api.json()["item"]
    return bucket_list_item


class Trivia:
    def __init__(self, category, difficulty, trivia_type):
        self.category = category
        self.difficulty = difficulty
        self.type = trivia_type

    def trivia_func(self):
        trivia_url = f"https://opentdb.com/api.php?amount=1&category={self.category}&difficulty={self.difficulty}&type={self.type}"
        trivia_api = requests.get(trivia_url).json()
        question_dict = trivia_api["results"][0]
        return question_dict


class Historical:
    def __init__(self, search_word):
        self.search_word = search_word

    def historical_event(self):
        event_url = f"https://api.api-ninjas.com/v1/historicalevents?text={self.search_word}"
        event_api = requests.get(event_url, headers={"X-Api-Key": "API KEY"})
        event_api.json = event_api.json()
        return event_api.json

    def historical_figure(self):
        figure_url = f"https://api.api-ninjas.com/v1/historicalfigures?name={self.search_word}"
        figure_api = requests.get(figure_url, headers={"X-Api-Key": "API KEY"})
        figure_api.json = figure_api.json()
        return figure_api.json


def useless_fact():
    useless_fact_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    useless_fact_api = requests.get(useless_fact_url)
    useless_fact_output = useless_fact_api.json()['text']
    return useless_fact_output
