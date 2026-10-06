import cv2

car_cascade=cv2.CascadeClassifier("cars.xml")

cap =cv2.VideoCapture("132849-754950619_small.mp4")

while True:
    ret,frame=cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=car_cascade.detectMultiScale(gray,1.1,1)

    car_count=len(cars)

    for x,y,w,h in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.putText(frame,"Cars detected:"+str(car_count),(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Car detection",frame)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()