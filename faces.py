def main():
    phrase=input("")
    print(convert(phrase))


def convert(phrase: str):
    phrase=phrase.replace(":)", "🙂").replace(":(", "🙁")
    return phrase
main()