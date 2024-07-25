def single_root_words(root_word, *other_words):
    same_words = []
    for el in other_words:
        if root_word.lower() in el.lower() or el.lower() in root_word.lower():
            same_words.append(el)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')