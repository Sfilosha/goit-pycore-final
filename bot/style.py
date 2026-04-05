from questionary import Style

custom_style = Style([
    ('question', 'bold'),               # question text
    ('answer', 'fg:#f44336 bold'),      # submitted answer text behind the question
    ('pointer', 'fg:#edf030 bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#edf030 bold'), # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
    ('separator', 'fg:#ffffff'),        # separator in lists
    ('instruction', 'fg:#737373'),      # user instructions for select, rawselect, checkbox
    ('text', ''),                       # plain text
    ('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
])