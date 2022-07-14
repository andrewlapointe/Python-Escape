class Display:

    def _formatString(string: str) -> str:
        new_string = f"-> {string}\n"

    def displayString(output: str) -> None:
        """
        Formats strings, and prints to console.

        Args:
            output (str): string to be formatted
        """
        if Display._checkInput(output):
            print(output)

    def _checkInput(string: str) -> bool:  # TODO fix this function
        return True
