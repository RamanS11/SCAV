import numpy as np

def RGB2YUV(color):

    YUV_color = np.zeros(np.size(color))
    YUV_color[0] = 0.257 * color[0] + 0.504 * color[1] + 0.098 * color[2] + 16/256
    YUV_color[1] = -0.148 * color[0] - 0.291 * color[1] + 0.439 * color[2] + 128/256
    YUV_color[2] = 0.439 * color[0] - 0.368 * color[1] - 0.071 * color[2] + 128/256

    return YUV_color

def YUV2RGB(YUV):

    RGB_color = np.zeros(np.size(YUV))

    RGB_color[0] = 1.164 * (YUV[0] - 16/256) + 1.596 * (YUV[2] - 0.5)
    RGB_color[1] = 1.164 * (YUV[0] - 16/256) - 0.813 * (YUV[2] - 0.5) - 0.391 * (YUV[1] - 0.5)
    RGB_color[2] = 1.164 * (YUV[0] - 16/256) + 2.018 * (YUV[1] - 0.5)

    return RGB_color

def main():

# RGB 2 YUV:

    print("Inserte el valor 'R' del color (de 0 a 255):")
    R = float(input())
    print("Inserte el valor 'G' del color (de 0 a 255):")
    G = float(input())
    print("Inserte el valor 'B' del color (de 0 a 255):")
    B = float(input())

    RGB_color = np.array([R, G, B])/256

    print("\nEl valor en YUV es:")
    convert = RGB2YUV(RGB_color)*256.0
    print(np.round(convert))

# YUV 2 RGB:

    print("Inserte el valor 'Y' del color (de 0 a 255):")
    Y = float(input())
    print("Inserte el valor 'U' del color (de 0 a 255):")
    U = float(input())
    print("Inserte el valor 'V' del color (de 0 a 255):")
    V = float(input())

    YUV_color = np.array([Y, U, V])/256

    print("\nEl valor en RGB es:")
    convert = YUV2RGB(YUV_color)*256.0
    print(np.round(convert))

main()