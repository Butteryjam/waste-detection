from django.shortcuts import render, redirect




        
        
           
from django.shortcuts import render
import numpy as np
import pyttsx3
import pygame

      
import firebase_admin
from firebase_admin import credentials,db



def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:/Users/svish/Music/WASTE DETECTION/DEPLOYMENT/PROJECT/APP/wastesegregate-43754-firebase-adminsdk-fbsvc-17556b9b06.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://wastesegregate-43754-default-rtdb.firebaseio.com/'  # Replace with your firebase database URL
        })

initialize_firebase()
ref = db.reference('license_plates')

from django.shortcuts import render
from django.utils import timezone
from APP.models import Detected



def update_firebase(class_name):
    ref = db.reference('predictions')
    data = {
        'data': class_name,
    }
    ref.set(data)

def Deploy_9(request):
    if request.method == 'POST':
        import cv2
        import math
        import cvzone
        import openpyxl
        import pygame
        from ultralytics import YOLO
        import firebase_admin
        from firebase_admin import credentials, db

       
    

        pygame.mixer.init()
        cap = cv2.VideoCapture(0)
        model = YOLO('APP/bio.pt')

        classnames = ['Biodegradable','Non-biodegradable']
        biodegradable_classes = ['Biodegradable']
        non_biodegradable_classes = ['Non-biodegradable']

        # Excel Setup
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Frame Number', 'Class', 'Confidence', 'Coordinates'])

        frame_number = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (640, 480))
            results = model(frame, stream=True)

            for result in results:
                boxes = result.boxes
                for box in boxes:
                    confidence = math.ceil(float(box.conf[0]) * 100)
                    Class = int(box.cls[0])

                    if confidence > 50:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        # Draw rectangle
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cvzone.putTextRect(
                            frame, f'{classnames[Class]} {confidence}%',
                            [x1 + 8, y1 + 40], scale=1.2, thickness=2,
                            colorT=(0, 0, 255), colorR=(255, 255, 255)
                        )

                        # ---------------- SAVE DETECTION ----------------
                        detected_class = classnames[Class]
                        frame_number += 1
                        coordinates = f'({x1}, {y1}) to ({x2}, {y2})'

                        Detected.objects.create(
                            frame_number=frame_number,
                            class_name=detected_class,
                            confidence=confidence,
                            coordinates=coordinates,
                            timestamp=timezone.now()
                        )

                        print(f"Detected: {detected_class}, Confidence: {confidence}, Coordinates: {coordinates}")

                      
                        # Initialize Firebase only once
                        initialize_firebase()

                        # Connect to Firebase
                        ref = db.reference('predictions')

                        
                        if detected_class in biodegradable_classes:
                            branch = 'A'
                            movement_direction = "A" 
                        else:
                            branch = 'B'
                            movement_direction = "B" 

                        update_firebase(movement_direction)


                    else:
                        print("Low confidence detection ignored")

            cv2.imshow('Waste Detection', frame)
            key = cv2.waitKey(1)
            if key == 27:  # ESC to quit
                break

        cap.release()
        cv2.destroyAllWindows()

        saved_animals = Detected.objects.all()
        return render(request, '9_Deploy.html', {"saved_animals": saved_animals})

    else:
        return render(request, '9_Deploy.html')



def Per_Database_10(request):
    models = Detected.objects.all()
    return render(request, '10_Per_Database.html', {'models': models})
