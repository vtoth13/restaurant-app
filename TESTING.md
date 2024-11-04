# Testing

## Manuel Testing

| Page             | User Actions                                     | Expected Results                                                                                 | Y/N | Comments                       |
|------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------|-----|---------------------------------|
| Home Page        | Open the home page                               | Page loads with clear options: "Book a Table," "View Menu," "Contact Info," and "Opening Hours."| Y   |                                |
|                  | Click on "Book a Table"                          | Redirects to the booking page                                                                   | Y   |                                |
|                  | Click on "View Menu"                             | Redirects to menu page with all items displayed                                                 | Y   |                                |
|                  | Check if "Opening Hours" section is visible      | Displays accurate opening hours                                                                | Y   |                                |
|                  | Verify "Contact Information" section             | Contact phone number and address are visible and accurate                                       | Y   |                                |
| Tables Page      | Open the "Tables" page                           | Loads with a list of tables showing number, capacity, and current availability status           | Y   |                                |
|                  | Verify table availability status                 | Displays correct status (Available/Occupied)                                                    | Y   |                                |
|                  | Click on an available table                      | Prompts user to log in if not authenticated                                                     | Y   |                                |
|                  | Attempt to view details on an occupied table     | Shows status as "Occupied" without option to book                                               | Y   |                                |
|                  | Verify display of restaurant opening hours       | Hours of operation are clearly displayed                                                       | Y   |                                |
|                  | Check for contact details on page                | Displays restaurant contact number and address                                                  | Y   |                                |
| Booking Process  | Select date and time for booking                 | Date and time selection available within restaurant operating hours                             | Y   |                                |
|                  | Attempt booking without selecting date/time      | Displays error message requiring date and time selection                                        | Y   |                                |
|                  | Confirm booking with valid date/time selection   | Shows booking confirmation message and booking summary                                          | Y   |                                |
| Menu Page        | Open "Menu" page                                 | Loads with a list of food and drink items, each with name, description, price, and image        | Y   |                                |
|                  | Click on menu item                               | Expands item details, showing additional description if available                               | Y   |                                |
|                  | Verify images load correctly for each item       | Each item has a properly loaded image                                                           | Y   |                                |
|                  | Verify all prices and descriptions are visible   | All items display names, descriptions, and prices                                               | Y   |                                |
| Sign Up Page     | Open "Sign Up" page                              | Displays fields for username, email, password, and password confirmation                        | Y   |                                |
|                  | Enter valid username                             | Field accepts up to 150 characters                                                             | Y   |                                |
|                  | Enter username with special characters           | Rejects input, displays error for invalid characters                                           | Y   |                                |
|                  | Enter valid email                                | Accepts input only in valid email format                                                        | Y   |                                |
|                  | Enter invalid email format                       | Displays error message for incorrect email format                                               | Y   |                                |
|                  | Enter valid password                             | Accepts secure password within criteria (8+ chars, alphanumeric, etc.)                          | Y   |                                |
|                  | Enter weak or short password                     | Displays error for insufficient password security                                               | Y   |                                |
|                  | Confirm password with mismatched entry           | Shows error indicating passwords must match                                                     | Y   |                                |
|                  | Click "Sign Up" with valid inputs                | Redirects to account confirmation page or welcome screen                                        | Y   |                                |
|                  | Click "Sign Up" with incomplete form             | Shows field-specific error messages                                                             | Y   |                                |
| Create Booking   | Open "Create Booking" page                       | Redirects to login page if not authenticated                                                    | Y   |                                |
|                  | Log in as authenticated user                     | Accesses the booking form page directly after login                                             | Y   |                                |
|                  | Select table from dropdown                       | Dropdown shows only available tables within selected time                                       | Y   |                                |
|                  | Enter guest count                                | Field validates input to stay within table capacity                                             | Y   |                                |
|                  | Click "Confirm Booking"                          | Success message shown; booking details saved to user account                                    | Y   |                                |
|                  | Attempt double-booking at same time              | Error displayed if table is unavailable at selected time                                        | Y   |                                |
| My Bookings      | Open "My Bookings" page                          | Redirects to login page if not authenticated                                                    | Y   |                                |
|                  | View list of bookings                            | All current bookings display with date, time, table, and guest count                            | Y   |                                |
|                  | Click "Edit" on a booking                        | Redirects to pre-filled edit form                                                               | Y   |                                |
|                  | Make and save changes to booking                 | Success message displayed; updated booking details shown                                        | Y   |                                |
|                  | Click "Cancel" on a booking                      | Prompts confirmation; removes booking upon confirmation                                         | Y   |                                |
|                  | Attempt to edit or cancel past booking           | Error or restriction prevents modifying past bookings                                           | Y   |                                |
| Login Page       | Open "Login" page                                | Page loads with fields for email/username and password                                         | Y   |                                |
|                  | Enter valid email and password                   | Redirects to user dashboard on successful login                                                 | Y   |                                |
|                  | Enter incorrect email/password                   | Displays error message for incorrect credentials                                                | Y   |                                |
|                  | Leave fields empty and attempt login             | Error message prompts user to fill required fields                                              | Y   |                                |
| Responsiveness   | Open each page on mobile                         | Layout adapts for smaller screens, all elements are accessible and readable                     | Y   | Verified across all pages      |
|                  | Verify functionality of interactive elements     | Buttons, dropdowns, and input fields are fully functional on mobile                             | Y   |                                |
|                  | Check "Menu" and "Tables" page on tablet         | Layout remains accessible and formatted for tablet screen size                                  | Y   |                                |
