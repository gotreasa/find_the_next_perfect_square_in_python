from modules import find_next_perfect_square


def describe_dummy_kata():
    def should_print_title(capsys):
        """🧪 expect the dummy kata prints the title"""
        find_next_perfect_square.print_the_title()
        out, _err = capsys.readouterr()
        assert "😊 Welcome to Dummy Kata" in out
