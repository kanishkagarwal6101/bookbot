def get_num_words(content):
    return len(content.split())

def count_characters(text):
    text = text.lower()
    obj = {}
    for ch in text:
        if ch in obj:
            obj[ch] += 1
        else:
            obj[ch] = 1
    return obj

def sort_on(item):
    return item["num"]

def sort_map(map):
    sorted_list = []
    for ch in map:
        sorted_list.append({"char": ch, "num": map[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

