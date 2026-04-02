"""Starter code for the Python Data Structures assignment."""


def average_grade(grades):
    # TODO: Return the average value of the grades list.
    pass


def highest_grade(grades):
    # TODO: Return the highest grade in the grades list.
    pass


def word_stats(words):
    # TODO: Return a dictionary with total_words, unique_words, and frequencies.
    # Example:
    # {
    #     "total_words": 5,
    #     "unique_words": 3,
    #     "frequencies": {"python": 2, "lista": 2, "tupla": 1}
    # }
    pass


def main():
    grades = [8.5, 7.0, 9.2, 6.8]
    subjects = ("Matematica", "Ciencias", "Programacao")
    words = ["python", "lista", "python", "tupla", "lista"]

    print("Average:", average_grade(grades))
    print("Highest:", highest_grade(grades))

    print("Subjects:")
    for subject in subjects:
        print("-", subject)

    print("Word stats:", word_stats(words))


if __name__ == "__main__":
    main()
