def generate_bc(url, separator):
    way_list = url.split('/')

    a = ('<a href="/', '">', '</a>')
    span = ('<span class="active">', '</span>')
    sep = ' ' + separator + ' '
    way = '<a href="/">HOME</a>'
    way_point = ''
    link = False
    index = False

    if 'index.' in way_list[-1]:
        index = True
    else:
        for i in '.=?#':
            if i in way_list[-1]:
                link = True
                way_list [-1] = way_list[-1].split(i)[0]

    for i in range(1, len(way_list)):
        way += sep
        way_point += way_list[i] + '/'

        if index and ((i == len(way_list) - 2) or (len(way_list)) == 2):
            way += span[0] + way_list[i].upper() + span[1]
            break

        if link and (i == len(way_list) - 1):
            way += span[0] + way_list[i].upper() + span[1]
        else:
            way += a[0] + way_point + a[1] + way_list[i].upper() + a[2]
    return way

a = [("mysite.com/pictures/holidays.html", " : "),
     ("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "),
     ("www.microsoft.com/important/confidential/docs/index.htm#top", " * "),
     ("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "),
     ("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ")]
for i in a:
    print(generate_bc(i[0], i[1]))