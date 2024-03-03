from django.shortcuts import render, redirect
import requests
from PIL import Image
from .pipeline import loaded_pipeline as pipeline
from math import ceil
from .models import ImagePicker, VideoPicker, AudioPicker
from statistics import mean
import os
from datetime import datetime
from .audio import inspect_audio

def home(request):
    return render(request, 'predictor/index.html')

def inspect(request):
    for file in os.listdir('Glitch_FakeWatch/static/img/'):
        if file.startswith('face_'):
            os.remove('Glitch_FakeWatch/static/img/'+file)
    if os.path.exists('Glitch_FakeWatch/media/'):
        for file in os.listdir('Glitch_FakeWatch/media/'):
            os.remove('Glitch_FakeWatch/media/'+file)
    if os.path.exists('Glitch_FakeWatch/static/img/input_img.jpeg'):
        os.remove('Glitch_FakeWatch/static/img/input_img.jpeg')
    if request.method == 'POST':
        file_input = request.FILES.get('file_input')
        if file_input == '':
            return render(request, 'predictor/inspect.html', {'error': 'Please choose the image/video before proceeding'})
        else:
            content_type = file_input.content_type
            if "image" in content_type:
                image = ImagePicker(image = file_input)
                image.save()
                im = Image.open(image.image)
                im.save('../Glitch_FakeWatch/static/input_img.jpeg')
                if im.mode == 'CMYK':
                    im = im.convert('RGB')
                result = pipeline.predict(image_path=im)
                return inspectionReport(request, result)
            elif "video" in content_type:
                video = VideoPicker(video = file_input)
                video.save()
                result = pipeline.predict_video(video_path="../Glitch_FakeWatch"+video.get_url())
                return inspectionReport(request, result)
            elif "audio" in content_type:
                audio = AudioPicker(audio = file_input)
                audio.save()
                print(audio.get_url())
                result = inspect_audio("../Glitch_FakeWatch"+audio.get_url())
                return audio_inspection(request, result)              
            else:
                return render(request, 'predictor/inspect.html', {'error': 'Please choose the image/video file'})
    return render(request, 'predictor/inspect.html')

def inspectionReport(request, result):
    faces = result['faces']
    scores = result['scores']
    overall_score = mean(scores) * 100
    overall_other_score = 100.0 - overall_score
    overall_score = str(overall_score)
    overall_score = overall_score[:overall_score.index('.')+3]
    overall_other_score = str(overall_other_score)
    overall_other_score = overall_other_score[:overall_other_score.index('.')+3]
    i=0
    for face in faces:
        face.save('static/img/face_{0}.jpeg'.format(i))
        i += 1
    st = []
    max_photos = min(i, 8)
    for c in range(max_photos):
        img = 'img/face_{0}.jpeg'.format(c)
        count = c
        color = 'auto'
        if scores[c] > 0.50:
            color = 'red'
        else: 
            color = 'green'
        face_score = str(scores[c] * 100)
        face_score = face_score[:face_score.index('.')+3]
        st.append({'image':img, 'count':count, 'score': str(face_score) + ' %', 'color': color})
    return render(request, 'predictor/select.html', {'faces': st, 'overall_score': overall_score, 'overall_other_score': overall_other_score, 'date': datetime.now()})

def audio_inspection(request, result):
    result = result * 100
    result = str(result)
    result = result[:result.index('.')+3]
    return render(request, 'predictor/audio.html', {'result': result})