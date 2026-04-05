import bot.helpers.logger as logger

@logger.input_error
def parse_input(user_input):
    if not user_input.strip():
        raise ValueError
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args