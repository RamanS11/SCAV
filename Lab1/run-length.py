from pip._vendor.distlib.compat import raw_input
import binascii

def rle_encode(data):
    # Declare the variables we'll use
    data = str(data[0])     # As we are pasing a list, we need to get the fistr element (the only one), if we do not do this
                            # the process will not work as we want (the iteration will be over the list, and the function will
    encoding = ''           # return the sequence indicating that it appears one time.
    prev_char = ''
    count = 1

    if not data: return ''
    print(data)
    for int in data:
        # If the prev and current characters
        # don't match...
        if int != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += prev_char + str(count)
            count = 1
            prev_char = int
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += prev_char + str(count)
        return [encoding]

def main():

    print("Introduce a bytes sequence separate with spaces: ")  # Get the user's input (must be sequence separated with spaces)
    a = input()

    myIntegers = [str(x) for x in a.split()]                    # Split each of the hexadecimals

    code = []
    for i in range(len(myIntegers)):

        aux = "{0:08b}".format(int(hex(int(myIntegers[i], 16)), 16))    # Convert the input to a binari sequence.
        print("\nInput: "+str(i+1)+" in hexadecimal: "+hex(int(myIntegers[i], 16))+". Binari sequence: "+aux)

        code.append(rle_encode([aux]))                                  # Call the function that computes the RLE with the binari sequence.

        print("Encoding (RLE): "+str(code[i]))

    print("\nEncoding: "+str(code))

main()