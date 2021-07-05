import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# playing with updating a shelf
with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup

    # this does not update the shelf without 'writeback=True'
    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    # a new assignment to recipes will trigger a write action
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    for snack in recipes:
        print(snack, recipes[snack])

# using 'writeback' modifications of the 'recipes' shelf are persisted
# data is cached and written only after closing the shelf
with shelve.open("recipes", writeback=True) as recipes:
    recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])

# example for wrongly using the sync() method
with shelve.open("./fileio/recipes", writeback=True) as recipes:
    recipes["soup"] = soup
    recipes.sync()  # this removes the 'soup' from the cache which is why the next line doesn't do anything
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])


