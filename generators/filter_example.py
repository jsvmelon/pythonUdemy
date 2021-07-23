import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]


def spamless_for():
    result = []
    for meal in menu:
        if "spam" not in meal:
            result.append(meal)
    return result


def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]  # this is more comparable to the filter
    return meals


def not_spam(meal_list: list):
    return "spam" not in meal_list


def spamless_filter():
    spam_less_meals = list(filter(not_spam, menu))
    return spam_less_meals


if __name__ == "__main__":
    print(spamless_for())
    print("-" * 40)
    print(spamless_comp())
    print("-" * 40)
    print(spamless_filter())
    print("-" * 40)
    print(timeit.timeit(spamless_for, number=1000000))
    print(timeit.timeit(spamless_comp, number=1000000))
    print(timeit.timeit(spamless_filter, number=1000000))
