# Created by Ryan Nguyen
# Created on December 2020
# This program cycles through all rgb values


def main():
    # This function prints rgb alues

    counter1 = 0
    counter2 = 0
    counter3 = 0
    # no input

    # process + output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({},{},{})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
