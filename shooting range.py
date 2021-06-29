def short_name(name):
    if len(name) > 30:
        name_words = name.split('-')
        name = ''
        for i in name_words:
            if i.lower() not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]:
                name += i[0]
    return name.upper()


print(short_name('very-long-url-to-make-a-silly-yet-meaningful-example'))