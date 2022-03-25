## Questions

- If pytest also depends on the python version setup, can we use docker to test it instead to make sure our package is tested on simple? 
- Why we need `__init__.py` file inside both module folder and tests folder
  - Consult [pytest best practices](https://docs.pytest.org/en/latest/goodpractices.html)
- Should we use relative import in testing
  - Use relative to make sure the imported is the one on development not one you install.

## Learning

- The format of testing help people understand how a code is structured.
- pytest function has no arguemenet by default because unit test should be isolated.
- pytest should be testing packages in editable install mode.
- Assertion in function should be minimal as the testing supposed to be inside the testing code
- What to keep in mind in testing
  - Does it run at all?
  - Refactoring your code, because unit testing keep your code do the things its suppposed to
  - Does it passes basic knowledge
  - Helps people understand what your library doing
- If your function/module is 

> Split up `requirements.txt` and `requirements-dev.txt`
> Compilation is a part of test (which they check a types etc.)
### Fixtures

Because sometime there's an external or setup phases that needs long time to load (loading data, calling API, etc.) and we call it multiple times in our tests the time will be multiplied. Using `fixtures` we can do the slow operation only once for multiple unit tests whithout the hassle of juggling global variables.

> What's the meaning of scope for `fixtures`?  
By default its used to reuse one object or process that needs a long time to run or initiate.

> Any best practice on naming `fixtures`? And whats the differences between it and mocks?

Some example:
- Spark Cluster
- Database

### Mock

Fake out the object and add the little thing that we actually needs. For example:

- Fitting a model could take hours, and in this case we need to test `.fit()` we could mock the rest of the model.
- Calling an API, because twitter and google limit their API and mocks helps us fake http requests.
- Database response, useful especially since it's not good to have access to production DB.

In his example he used dataframe as example, but how to use it properly test? We could add function to an attribute(?)

- Can we make Mock inherit an object functionality
- How to prevent ourself cheating in Mocking?

### Patch

`monkeypatch` is fixture in `pytest` that can be used to patch a certain method from package imported in our module.

## Any Examples using Pytest?

- Arviz : using travis 200~ unit tests (on smaller side)
- Pandas