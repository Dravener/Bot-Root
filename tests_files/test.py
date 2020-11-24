from pytesseract import Output
import pytesseract
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="screenshot1.png")
ap.add_argument("-c", "--min-conf", type=int, default=0, help="26")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
for i in range(0, len(results["text"])):
    # extract the bounding box coordinates of the text region from
    # the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    # extract the OCR text itself along with the confidence of the
    # text localization
    text = results["text"][i]
    conf = int(results["conf"][i])
    # filter out weak confidence text localizations
    if conf > args["min_conf"]:
        # display the confidence and text to our terminal
        print("Confidence: {}".format(conf))
        print("Text: {}".format(text))
        print("")
        # strip out non-ASCII text so we can draw the text on the image
        # using OpenCV, then draw a bounding box around the text along
        # with the text itself
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 0, 255), 3)
    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# find all elements in page
# elements = driver.find_elements_by_css_selector('*')
# for element in elements:
#     # check if element has text
#     if not element.text:
#         text_to_be_summarized += ''
#     else:
#         # se_text = re.findall('^def.*\n\s{4}.*$', element.text)
#         # print(se_text)
#         reg_patter = ".*\n((\s{2})|(\s{4})).*"
#         findings = re.findall(reg_patter, element.text)
#         print(findings)
#         text_to_be_summarized += element.text
#         text_for_each_page += element.text