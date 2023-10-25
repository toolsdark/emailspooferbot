
# Create a custom keyboard with buttons
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
testing_button = types.KeyboardButton('/testing')
help_button = types.KeyboardButton('/help')
pricing_button = types.KeyboardButton('/pricing')
get_license_button = types.KeyboardButton('/getlicense')  # Add the "Get License" button
keyboard.row(testing_button, get_license_button)  # Include the "Get License" button in the same row
keyboard.row(help_button, pricing_button)  # Include the other buttons in the second row

# If you want whole source code please contact me for purchasing --> @toolsdark
