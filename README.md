![HBnB Logo](./logo/hbnb_logo.png)

#AirBnB_clone
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.
Have a good day

## Reporitory Contents

Its the following files:

| **File**                                                                     | **Description**                                                                                                          |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [AUTHORS](./AUTHORS)                                                         | Contains info about authors of the project                                                                               |
| [base_model.py](./models/base_model.py)                                      | Defines BaseModel class (parent class), and methods                                                                      |
| [user.py](./models/user.py)                                                  | Defines subclass User                                                                                                    |
| [amenity.py](./models/amenity.py)                                            | Defines subclass Amenity                                                                                                 |
| [city.py](./models/city.py)                                                  | Defines subclass City                                                                                                    |
| [place.py](./models/place.py)                                                | Defines subclass Place                                                                                                   |
| [review.py](./models/review.py)                                              | Defines subclass Review                                                                                                  |
| [state.py](./models/state.py)                                                | Defines subclass State                                                                                                   |
| [file_storage.py](./models/engine/file_storage.py)                           | Creates new instance of class, serializes and deserializes data                                                          |
| [console.py](./console.py)                                                   | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
| [test_base_model.py](./tests/test_models/test_base_model.py)                 | unittests for base_model                                                                                                 |
| [test_user.py](./tests/test_models/test_user.py)                             | unittests for user                                                                                                       |
| [test_amenity.py](./tests/test_models/test_amenity.py)                       | unittests for amenity                                                                                                    |
| [test_city.py](./tests/test_models/test_city.py)                             | unittests for city                                                                                                       |
| [test_place.py](./tests/test_models/test_place.py)                           | unittests for place                                                                                                      |
| [test_review.py](./tests/test_models/test_review.py)                         | unittests for review                                                                                                     |
| [test_state.py](./tests/test_models/test_state.py)                           | unittests for state                                                                                                      |
| [test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage                                                                                               |
| [test_console.py](./tests/test_console.py)                                   | unittests for console                                                                                                    |

### Usage

| **Method**                | **Description**                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [create](./console.py)    | Creates object of given class                                                                                           |
| [show](./console.py)      | Prints the string representation of an instance based on the class name and id                                          |
| [all](./console.py)       | Prints all string representation of all instances based or not on the class name                                        |
| [update](./console.py)    | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
| [destroy](./console.py)   | Deletes an instance based on the class name and id (save the change into the JSON file)                                 |
| [count](./console.py)     | Retrieve the number of instances of a class                                                                             |
| [help](./console.py)      | Prints information about specific command                                                                               |
| [quit/ EOF](./console.py) | Exit the program                                                                                                        |
