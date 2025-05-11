# AirBnB Clone - The Console

## Description
This project is the first step in building a full web application for an AirBnB clone. It consists of a command-line interpreter that allows users to create, update, delete, and manage objects related to the AirBnB system, such as users, places, cities, and more.

The command interpreter provides functionalities to:
- Create new objects (e.g., User, Place)
- Retrieve objects from storage
- Update object attributes
- Delete objects
- Perform operations such as counting and computing statistics

## Features
- Custom command-line interface using Python's `cmd` module
- Serialization and deserialization of objects using JSON
- A base model class that handles unique IDs, timestamps, and persistence
- Unit testing using `unittest` framework

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/iclaudiaadeline/alu-AirBnB_clone.git
   cd AirBnB_clone
   ```
2. Ensure you have Python 3.8+ installed.
3. Make the console executable:
   ```sh
   chmod +x console.py
   ```

## Usage
### Interactive Mode
Run the command interpreter in interactive mode:
```sh
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode
Run the console with a command:
```sh
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

## File Structure
```
AirBnB_clone/
├── console.py          # Command interpreter
├── models/
│   ├── __init__.py     # Initializes models package
│   ├── base_model.py   # BaseModel class
│   ├── user.py         # User class (inherits from BaseModel)
│   ├── place.py        # Place class (inherits from BaseModel)
│   ├── city.py         # City class (inherits from BaseModel)
│   ├── state.py        # State class (inherits from BaseModel)
│   ├── amenity.py      # Amenity class (inherits from BaseModel)
│   ├── review.py       # Review class (inherits from BaseModel)
│   ├── engine/
│   │   ├── file_storage.py  # Handles object storage in JSON format
│   │   └── __init__.py      # Initializes storage engine
├── tests/
│   ├── test_models/
│   │   ├── test_base_model.py  # Unit tests for BaseModel
│   │   ├── test_user.py        # Unit tests for User
│   │   ├── ...
├── README.md
├── AUTHORS
├── requirements.txt
```

## Testing
Run all unit tests using:
```sh
python3 -m unittest discover tests
```
Run a specific test file:
```sh
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
Adeline Claudia IRADUKUNDA 


