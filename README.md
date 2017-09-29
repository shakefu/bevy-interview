# bevy-interview
Code from doing the Bevy interview.

## Usage

This script will print out all permutations of a string, one per line. It also
exports an API for doing this in code.

Check out the repository and run with:

```bash
python main.py [arg]
```

... Where argument is a string

### Running tests

First install the `nose` package:

```bash
pip install nose
```

Then run nosetests:

```bash
nosestests -vs test/
```


## API documentation

This package exports one module, poorly named "main".

### `main.permute(`*`arg`*`)`

Returns a list of permutations of the string `arg`.

-  **arg** (*str*) - A string to permute



