import random


def qte():
    arr_keys = {"a": "A", "c": "C", "e": "E", "v": "V", "K_SPACE": "SPACE"}
    choice = random.choice(list(arr_keys.keys()))
    print(choice)
    print(arr_keys[choice])


def main() -> None:
    qte()


if __name__ == "__main__":
    main()
