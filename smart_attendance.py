#importing librariesimport face_recognitionimportcv2
importnumpyasnpimportcsv
importos
fromdatetimeimportdatetime

# Getareferenceto webcam#0(thedefaultone)
video_capture=cv2.VideoCapture(0)

# Loadasamplepictureandlearnhow torecognize it.druva_image = face_recognition.load_image_file("photos/druva.jpg")druva_encoding=face_recognition.face_encodings(druva_image)[0]

Rahul_image=face_recognition.load_image_file("photos/Rahul.jpg")rahul_encoding=face_recognition.face_encodings(rahul_image)[0]

sathwik_image =face_recognition.load_image_file("photos/sathwik.jpg")sathwik_encoding=face_recognition.face_encodings(sathwik_image)[0]

varun_image=face_recognition.load_image_file("photos/varun.jpg")varun_encoding=face_recognition.face_encodings(varun_image)[0]

#Createarraysofknown faceencodingsandtheirnames
known_face_encoding = [druva_encoding,rahul_encoding,sathwik_encoding,varun_encoding
]
known_faces_names=d"druva",
"rahul","sathwik","varun"
students=known_faces_names.copy()

#Initializesomevariablesface_locations=[]face_encodings =[]face_names=[]
s=True

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

f=open(current_date+'.csv','w+',newline='')Inwriter= csv.writer(f)
whileTrue:

#Grab asingleframeofvideo
_,frame=video_capture.read()

#Resizeframeofvideoto1/4sizeforfasterfacerecognitionprocessing
small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

# ConverttheimagefromBGRcolor(whichOpenCVuses)toRGBcolor(whichface_recognitionuses)
rgb_small_frame = small_frame[:,:,::-1]ifs:

#Findallthefacesand faceencodingsinthecurrentframeofvideo
face_locations=face_recognition.face_locations(rgb_small_frame)
face_encodings=face_recognition.face_encodings(rgb_small_frame, face_locations)face_names=[]
forface_encodinginface_encodings:

#Seeifthefaceisa matchfortheknownfaces
matches=face_recognition.compare_faces(known_face_encoding,face_encoding)name =""
face_distance =face_recognition.face_distance (known_face_encoding, face_encoding)best_match_index=np.argmin(face_distance)
ifmatches[best_match_index]:
name=known_faces_names[best_match_index]face_names.append(name)
ifnameinknown_faces_names:ifnameinstudents:
students.remove(name)print(students)
current_time=now.strftime("%H-%M-%S")Inwriter.writerow([name,current_time])
cv2.imshow("attendencesystem",frame)ifcv2.waitkey(1)&0xFF==ord('q'):
break

# Release handle to the webcamvideo_capture.release()cv2.destroyAllWindows()f.close()