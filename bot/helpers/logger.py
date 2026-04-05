from typing import Callable
from colorama import init, Fore
from bot.models.Errors import NotFoundError

init()

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError as e:
            return (Fore.RED + {e})
        except ValueError as e:
            return (Fore.RED + str(e)) if str(e) else "Incorrect value is provided"
        except KeyError as e:
            return (Fore.RED + str(e)) if str(e) else "Item not found."
        except IndexError:
            return (Fore.RED + "Invalid command")
        except Exception as e:
            return (Fore.RED + f"An unexpected error occurred: {e}")
    return inner