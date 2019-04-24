FROM ekholabs/face-classifier


RUN pip3 install requests
ADD src/web/emotion_gender_processor.py /ekholabs/face-classifier/src/web/
ADD src/web/faces.py /ekholabs/face-classifier/src/web/

ENTRYPOINT ["python3"]
CMD ["src/web/faces.py"]
