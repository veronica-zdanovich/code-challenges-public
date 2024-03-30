def stories(endings, choices, option):
    max_elem = endings[-1]
    pages = [i for i in range(0, max_elem + 1)]
    choices_list = [choice[0] for choice in choices]
    page_index = 1  # first element - 1

    while page_index <= max_elem:
        if page_index < 0:  # already visited
            return -1

        if pages[page_index] < 0:  # already visited
            return -1

        if pages[page_index] in endings:  # ending reached
            return pages[page_index]

        if pages[page_index] in choices_list:
            choice_index = choices_list.index(pages[page_index])
            choice = choices[choice_index]
            pages[page_index] = -1

            if option == 1:
                page_index = pages[choice[1]]
            else:
                page_index = pages[choice[2]]
        else:
            pages[page_index] = -1
            page_index += 1

    return -1
