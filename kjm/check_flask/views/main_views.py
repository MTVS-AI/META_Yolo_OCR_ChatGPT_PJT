from flask import Blueprint
from flask import request
import os


bp = Blueprint('main',__name__,url_prefix='/')


#TODO YOLO & OCR & GPT
@bp.route('/ocr', methods=['GET', 'POST'])
def ocr():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if not allowed_file(file.filename):
        return "Invalid image format", 400

    # 고유한 파일명 생성
    ext = os.path.splitext(file.filename)[1]
    unique_filename = str(uuid.uuid4()) + ext
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

    file.save(filepath)

    # run_all 함수 호출
    analyzer = ImageProcess('best.pt', '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',
                        'https://fsjr0lq9ke.apigw.ntruss.com/custom/v1/24396/82f04b3aebc287bf6b01f1571df49417fd2b38cb145fa7f9aadbb152eacbb606/general',
                        'R1prcGNuRUthUG5hdGJPUW1Xd3pDVlVLUXdJZEx6UFM=')
    df_report = analyzer.run_all([filepath], 'capture_data/meta_data.json') # JSON_PATH는 적절한 경로로 대체하세요.
    # os.remove(filepath)  # OCR 처리된 이미지 파일 삭제 (필요하다면 주석 해제)
    return jsonify({'categories': df_report.categories})







# from flask import Blueprint
# from flask import request
# from Pybo.models import Question,Answer
# from datetime import datetime
# from Pybo import db
# import torch
# from torchvision import transforms
# from PIL import Image

# bp = Blueprint('classification',__name__,url_prefix='/classification')

# model = torch.load('model.pt',map_location=torch.device('cpu'))

# @bp.route('/catdog')
# def classification_catdog():
#   result = request.form
#   print(result)
#   print(result['chat'])
#   return '고양이 입니다.'

# @bp.route('/birdflower')
# def classification_birdflower():
#     q = Question(subject='질문1',content='고양이 맞나요?',create_date = datetime.now())
#     db.session.add(q)
#     db.session.commit()
#     return '비둘기 입니다.'

# @bp.route('/get_question')
# def get_question():
#     #questions = Question.query.all() #[questions1,qustion2,....]
#     #print(len(questions))
#     #result = Question.query.filter(Question.content.like('%고양이%')).all()
#     #print(result[0].subject)
#     #print(result[0].content)
#     #result = Question.query.get(1)
#     #result.subject = '제목을 바꿈 1'
#     #db.session.commit()
#     result = Question.query.get(1)
#     db.session.delete(result)
#     db.session.commit()
#     return '가져오기 성공'


# @bp.route('/manwomen')
# def classification_manwomen():
#  return '여성 입니다.'

# @bp.route('/makale',methods=['POST'])
# def classification_makale():
#     print(request.files)
#     f = request.files['image']
#     print(f.filename)
#     f.save('image.jpg')
#     image = Image.open('image.jpg')

#     transform_test = transforms.Compose([
#         transforms.Resize((224,224)),
#         transforms.ToTensor(),
#         transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
#     ])

#     image = transform_test(image).unsqueeze(0).to('cpu')
#     model.to('cpu')
#     with torch.no_grad():
#         outputs = model(image)
#         print(outputs)
#         _, preds = torch.max(outputs,1)
#         classname = ['마동석','이국주','카리나']
#         print(classname[preds[0]])
#     return classname[preds[0]]+' 입니다.'