import subprocess

from num2words import num2words


def say(number: int) -> str:
    """
    Say the number in words

    :param
    number: int

    :return:
    sentence: str
    """
    if 0 <= number < 1000000000000:
        sentence = num2words(number).split()

        for index, word in enumerate(sentence):
            if word == "and":
                sentence.pop(index)
            elif word.endswith(","):
                sentence[index] = word.replace(",", "")

        subprocess.run(["say", ' '.join(sentence)])  # Extension for Mac
        # subprocess.call(  # Extension for Linux
        #     "espeak",
        #     "-ven+f3 -k5 -s150 --punct='<characters>'",
        #     ' '.join(sentence),
        #     "2>>/dev/null"
        # )
        return ' '.join(sentence)
    else:
        raise ValueError(".+")
