"""
Command to print out all permutations of a string.

"""
# System libraries
import sys


"""
Returns all the permutations of the string `arg` in a list.

:param arg: A string to permutate

"""
def permute(arg):
    arg = list(arg)

    # If we only have one character, that's a termination condition for
    # recursion, just return is itself
    if len(arg) == 1:
        return arg

    # Array of permutation strings
    perms = set()


    # If we have more than one character, we recursively iterate over them,
    # building our permutations
    for char in arg:
        perm = ''
        perm += char

        # Copy the list of characters, so we don't accidentally mutate for
        # other recursions
        remaining = arg[:]
        remaining.remove(char)

        # Get the permutations of the remaining string
        result = permute(remaining)

        # Append our calculated permuations to our set of results
        for item in result:
            perms.add(perm + item)

    return list(perms)


"""
Main method, called when this script is run as a main module, rather than
imported.

"""
def main():
    if len(sys.argv) < 2:
        print "Missing argument string"
        sys.exit(1)

    if len(sys.argv) > 2:
        print "Too many arguments, I don't know what to do with them"
        sys.exit(1)

    # Get the permutations of the passed argument
    permutations = permute(sys.argv[1])

    for item in permutations:
        print item

    sys.exit(0)


# Only run the main script if we're running this as a main script, rather than
# importing it into tests or other packages
if __name__ == "__main__":
    main()

