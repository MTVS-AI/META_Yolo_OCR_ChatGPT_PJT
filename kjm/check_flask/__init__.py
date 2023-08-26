from flask import Flask, render_template
from flask import request
from werkzeug.utils import secure_filename
import os
import time
import uuid
import folium
import pandas as pd


from glob import glob

from .views.imgPro import ImageProcess as IP
# from .views.folium_map import MapManager as MM
from .views.folium_class_2 import MapManager as MM

def file_validation(filename):
    ALLOWED_EXTENSIONS = set(['jpg','JPG','png','PNG','mp4','json'])
    file_extension = filename.rsplit('.', 1)[1]
    return '.' in filename and file_extension in ALLOWED_EXTENSIONS , filename

app = Flask(__name__)

# ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'csv'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index_html():
    return render_template('13_upload.html')

# from .views import main_views
# app.register_blueprint(main_views.bp)


# @app.route('/ocr', methods=['GET', 'POST'])
# def ocr():
#     if 'file' not in request.files:
#         return "No file part", 400

#     file = request.files['file']

#     if file.filename == '':
#         return "No selected file", 400

#     if not allowed_file(file.filename):
#         return "Invalid image format", 400

#     # 고유한 파일명 생성
#     ext = os.path.splitext(file.filename)[1]
#     unique_filename = str(uuid.uuid4()) + ext
#     filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

#     file.save(filepath)

#     # run_all 함수 호출
#     analyzer = IP('','','')
#     df_report = analyzer.run_all([filepath], 'capture_data/meta_data.json') # JSON_PATH는 적절한 경로로 대체하세요.
#     # os.remove(filepath)  # OCR 처리된 이미지 파일 삭제 (필요하다면 주석 해제)
#     return jsonify({'categories': df_report.categories})








# check완 코드////////
@app.route('/ocr', methods=['GET', 'POST'])
def uploader_file():
#     # 파일 보내기 코드
#     # if request.method == 'POST':
#     #     file = request.files['file']
#     #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#     #     return 'file uploaded successfully'

    # 폴더 업로드 코드 
    if request.method == 'POST':
        files = request.files.getlist('file[]')
        print(files)
        for fil in files:
            filename = secure_filename(fil.filename)
            print(fil)
            print(filename)
            time.sleep(0.01)
            result,filename  = file_validation(filename)
            if result:
                fil.save(os.path.join('./check_flask/views/capture_data', filename))
        # IP괄호안 파라미터 3개 ////////
        aaa = IP('','','')
        # aaa.make_frame()
        # # aaa.move_all_img('C:/Users/user/Desktop/flask_12/check_flask/views/capture_data','C:/Users/user/Desktop/flask_12/temp' )
        # time.sleep(5)
        # # aaa.move_img('C:/Users/user/Desktop/flask_12/temp','C:/Users/user/Desktop/flask_12/check_flask/views/capture_data')
        # aaa.yolo_run()
        
        # imgs = glob('./check_flask/views/capture_data/*.jpg')
        # json_file_path = './check_0824_dfflask/views/capture_data/meta_data.json'
        # for idx,img in enumerate(imgs):
        #     # make_frame괄호속 파라미터 삭제
        #     df_report = aaa.make_frame()
        #     time.sleep(1)
        #     df_report = aaa.yolo_run(img, df_report)
        #     time.sleep(1)
        #     # print(df_report)
        #     idx = 15 # 추정되는 인덱스, 필요에 따라 조절 가능.
        #     df_report = aaa.clova_ocr_run(idx, df_report)
        #     time.sleep(1)
        #     df_report = aaa.chatGPT_run(idx,df_report)

        # 임시
        # df_report = pd.read_csv('./check_flask/views/reports/test_report_2023_08_12.csv')
        df_report = aaa.run_all(aaa.imgs, aaa.json_file_path)

        bbb = MM(df_report)
        bbb.create_folder(df_report)

        # MM.create_folder(df_report)
        # bbb.map.save('./check_flask/templates/Map.html')

        print('file uploaded successfully')
        return render_template('Map.html')


        
        
        
        
        