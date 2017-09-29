# bevy-interview
Code from doing Bevy interview

## Usage

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



