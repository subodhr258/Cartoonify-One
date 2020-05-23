import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#If you just want to input an image in your files:
#example: img = cv2.imread("adventure.jpeg")

while True: 
	# Capture frame-by-frame
	ret, img = cap.read()


	# 1) Edges
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 5)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

	# 2) Color
	color = cv2.bilateralFilter(img, 9, 300, 300)

	# 3) Cartoon
	cartoon = cv2.bitwise_and(color, color, mask=edges)


	#cv2.imshow("Image", img)
	#cv2.imshow("color", color)
	#cv2.imshow("edges", edges)
	cv2.imshow("Cartoon", cartoon)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()