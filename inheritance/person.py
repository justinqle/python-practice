class Person:
    """Represents a single human being."""

    def __init__(self, first_name, last_name):
        """Initialize

        first_name - first name
        last_name - last name
        """

        self.first_name = first_name
        self.last_name = last_name

    def _who(self):
        print(f'{self.first_name}:', end=' ')

    def speak(self, message):
        self._who()
        print(message)

    if __name__ == '__main__':
        print("Person Class")
