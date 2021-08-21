def recite(start_verse, end_verse):
    song = []
    animal = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    spider = " wriggled and jiggled and tickled inside her"
    line_2 = ['','',"How absurd","Imagine that,","What a hog,","Just opened her throat and","I don't know how she",""]
    for verses in range(start_verse, end_verse+1):
        if verses != 8:
            for verse in range(verses-1,-1,-1):
                if verse == verses-1:
                    song.append(f"I know an old lady who swallowed a {animal[verse]}.")
                    if verse == 0: pass
                    elif verse == 1:
                        song.append(f"It{spider}.")
                    elif 5 > verse > 1:
                        song.append(f"{line_2[verse]} to swallow a {animal[verse]}!")
                    else: song.append(f"{line_2[verse]} swallowed a {animal[verse]}!")
                elif verse == 1:
                    song.append(f"She swallowed the {animal[verse+1]} to catch the {animal[verse]} that{spider}.")
                else:
                    song.append(f"She swallowed the {animal[verse+1]} to catch the {animal[verse]}.")
            song.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        else:
            song.append(f"I know an old lady who swallowed a {animal[verses-1]}.")
            song.append("She's dead, of course!")
        if verses != end_verse: song.append("")
    return song