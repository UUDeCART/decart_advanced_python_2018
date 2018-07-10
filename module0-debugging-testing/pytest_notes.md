
### Using `tree`

I really love `tree` as a way of exploring my directories. Here is a command to list a directory structure with `tree` excluding files that match stuff I don't want to see:

```bash
tree -I "__pycache__|*egg*|build" .
```

[Here](https://superuser.com/questions/531592/how-do-i-add-the-tree-command-to-git-bash-on-windows) is a discussion about getting `tree` on Windows.

The easiest way to install `tree` on a Mac is with [home brew](https://brew.sh/), which I highly recommend installing.


On [this](https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules) web page is a description of different ways we can layout test code with pytest


### Testing Exceptions

In class we (I) struggled with how to test an exception. Based on [this](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest) Stackoverflow discussion, I came up with this test:

```Python
def test_vector_equality_unequal_length():
    v1 = [1,2,3]
    v2 = [1,2]

    with pytest.raises(ValueError):
        vec_eq(v1,v2)
```


#### Test Discovery

`pytest` will discover tests (functions and classes) by looking for functions and classes that start with `test` in files with names that start with `test`.

#### `PYTHONPATH` and which package am I testing?

* Do I want to test my installed version of the package or the uninstalled version?

* How does `pytest` determine paths?

### Using Virtual Environments with Anaconda
