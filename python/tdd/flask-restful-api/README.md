# NewStore Cloud Developer Task

## Introduction

**GOAL**: Deliver a small and simple flask-based RESTful-ish API for managing users

**Details**

* Store data however you want: csv, json, sqlite, mysql. Really, wherever you want. Keep it as simple as possible
* Show how you would write unit and/or functional tests for your application.
* Deliver as many of the user stories below as possible. But do not worry about getting all of them done. The focus here is to see your workflow.
* **Preferably** write your tests before writing application code, you will be asked about your thought process.
* You **must** deliver a functional test suite to prove that your RESTful API works


**Setting up your environment**

This challenge code is a basic [tumbler](https://github.com/gabrielfalcao/tumbler#1-install) web app, which is just a little wrapper around [flask](http://flask.pocoo.org/).

In order to get your environment up and running, make sure that you are working in a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). **Make sure that the the virtual env folder does not live in the same directory as this project**. In fact, you should just use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).

After your virtualenv is setup, install the dependencies by running:

```bash
make dependencies
```

The unit tests are located at `tests/unit/test_*.py`, similarly the functional tests are at `tests/unit/test_*.py`.

Run unit tests with

```bash
make unit
```

And functional tests with

```bash
make functional
```

**Reference/Documentation to help you**

* Write your assertions using [sure](https://github.com/gabrielfalcao/sure#installing), here is its [API Reference](https://github.com/gabrielfalcao/sure/blob/master/spec/reference.md)

* You can generate hashes using the [hashlib](https://docs.python.org/2/library/hashlib.html)
* If you decide to use a SQL database, you might want to use [SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)

## Ready to start ?

Here are the [user stories](http://martinfowler.com/bliki/GivenWhenThen.html) that
you need to deliver.

Imagine that you are already working at newstore and each story is a
tiket that you are closing in a normal day of work.


### Story 1: Create a simple endpoint that generates an md5 hash of an arbitrary email

```gherkin
Given the arbitrary email address "user@newstore.com"
When I POST a json payload with '{"data": "user@newstore.com"}' to the URL "/api/calculate-md5"
Then it should return a json that looks like this: '{"md5": "8c3a7ee05457d337d5bb14f438464cbf"}'
```

### Story 2: Build API endpoint that allows user creation

```gherkin
Given a JSON payload containing the fields:
  | field      | value            |
  | first_name | Guido            |
  | email      | guido@python.org |
  | password   | py123            |
When I POST on "/api/user"
Then it should store the user and return a JSON response with the fields:
  | field      | value                            |
  | uuid       | 02fd0bf3d9518a801517fd6fac005878 |
  | first_name | Guido                            |
  | email      | guido@python.org                 |
  | password   | py123                            |
And it should be stored in some sort of database
```

**NOTE:** generate the UUID with the algorithm:

```bash
uuid = md5digest("newstore:guido@python.org")
```

### Story 3: Build API endpoint for editing users

```gherkin
Given that the following users exist in the databse:
  | first_name | email            | password  |
  | Guido      | guido@python.org | py123     |
When I PUT on "/api/user/02fd0bf3d9518a801517fd6fac005878" with the a JSON payload containing:
  | field      | value       |
  | password   | securenow!  |
Then the database should have the users:
  | first_name | email            | password   |
  | Guido      | guido@python.org | securenow! |
```

### Story 4: Build API endpoint for retrieving a user

```gherkin
Given that the following users exist in the databse:
  | first_name | email            | password  |
  | Guido      | guido@python.org | py123     |
When I GET on "/api/user/02fd0bf3d9518a801517fd6fac005878"
Then it should return a JSON response with the user data
```

### Story 5: Build API endpoint for retrieving a list of users

```gherkin
Given that the following users exist in the databse:
  | first_name | email            | password  |
  | Guido      | guido@python.org | py123     |
  | Foo        | foo@bar.com      | foobar123 |

When I GET on "/api/users"
Then it should return a JSON response with a list of the existing users
```

### Story 6: Build API endpoint for removing users

```gherkin
Given that the following users exist in the databse:
  | first_name | email            | password  |
  | Guido      | guido@python.org | py123     |
  | Foo        | foo@bar.com      | foobar123 |
When I DELETE on "/api/user/guido@python.org"
Then it should return the deleted user info in the response
And now the database should only contain the users:
  | first_name | email            | password  |
  | Foo        | foo@bar.com      | foobar123 |
```

### BONUS goal: sketch out a frontend for one of your API endpoints

* Feel free to use AngularJS, backbone or whatever technologies. Create an interface that interacts with your API
* The boilerplate web app already renders the `index.html` file for you, feel free to include CDN-based dependencies to get your UI going.

To run the server use:

```bash
make run
```

You will see a basic template that you should be able to modify, at first it looks like this:

![screenshot.png](screenshot.png)


## Happy Hacking and good luck!
