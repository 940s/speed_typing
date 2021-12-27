# Vision

What is the vision of this product?

* A typing speed test that provides the user with words to type, accepts user input, compares it to the given words for accuracy and speed

What pain point does this project solve?

* Visualize and improve typing skills

Why should we care about your product?

* simple to use and feature rich

# Scope (In/Out)

## In

* provide the user with a series of words to type
* accept user input
* compare user input to provided words
* measure speed of user input
* display info to the user

## Out

* randomly generate words
* no multi-user support

# MVP

What will your MVP functionality be?

* static word display, accept input, measure/display input speed

What are your stretch goals?

* dynamic word display
* variable words to display
* statistics about user performance
* log in/out
* data persistance
* light mode/dark mode

# Functional Requirements

## MVP

* a user can run the program and see their speed

## Stretch

* An admin can create and delete user accounts
* A user can update their profile information
* A user can view individual statistics
    * fastest speed
    * accuracy
    * worst letters/words
    * change over time

# Data Flow

internal list of words -> display -> logic

user -> input -> logic

# Non-Functional Requirements

tested game logic and features
* ensure input is correctly compared to expected
* time is measured accurately
* wpm calculations