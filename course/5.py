import cv2

# # Chuyen tu anh mau sang anh cap xam
# fn = input("Enter the filename of the image to convert: ")
# img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
#
# if img is not None:
#     cv2.imshow('Image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Error: Could not read the image.")
#
#
# # Luu anh cap xam sang tep
# fn_new = "/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/anhxam.bmp"
# cv2.imwrite(fn_new, img)

# Chuyen tu anh mau sang anh nhi phan
# + Neu la anh mau 24 bit thi phai chuyen sang anh cap xam => chuyen sang anh nhi phan
# + Neu la anh cap xam chi chuyen ngay sang anh nhi phan

fn = input("Enter the filename of the image to convert: ")
img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)

if img is not None:
    img_binary = cv2.adaptiveThreshold(img, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                       thresholdType=cv2.THRESH_BINARY, blockSize=15, C=8)
    print(img_binary)
    cv2.imshow("Binary Image", img_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    fn_new = "/Users/cigrcham/Desktop/CodingWork/others/image_processing/image/image_binary.bmp"
    cv2.imwrite(fn_new, img_binary)
    print("Binary image saved as", fn_new)
else:
    print("Error: Could not read the image.")
