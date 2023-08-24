import branca
import numpy as np
from PIL import Image
import base64
import folium
import folium.plugins

def load_origin_img_path(load_df_report,idx):
    origin_img = eval(load_df_report.loc[idx,'Origin_img'])[0]
    origin_img = np.array(origin_img,dtype=np.uint8)
    img = Image.fromarray(origin_img)
    img_path = 'folium/origin_img.jpg'
    img.save(img_path, 'jpeg')

    return img_path

def load_detect_img_path(load_df_report,idx):
    detect_img = eval(load_df_report.loc[idx,'Detect_img'])
    detect_img = np.array(detect_img,dtype=np.uint8)
    img = Image.fromarray(detect_img)
    img_path = 'folium/detect_img.jpg'
    img.save(img_path, 'jpeg')

    return img_path

def load_crop_imgs_path(load_df_report,idx):
    crop_imgs = eval(load_df_report.loc[idx]['Crop_imgs'])
    n_crops = len(crop_imgs)
    crop_path_list = []

    for i in range(n_crops):
        crop_img = np.array(crop_imgs[i],dtype=np.uint8)
        img = Image.fromarray(crop_img)
        img_path = 'folium/crop_images_' + str(i) + '.jpg'
        img.save(img_path, 'jpeg')
        crop_path_list.append(img_path)

    return crop_path_list

def load_imgs_path(load_df_report, idx):
    base_path_list = []
    crop_path_list = []

    origin_img_path = load_origin_img_path(load_df_report, idx)
    detect_img_path = load_detect_img_path(load_df_report, idx)
    base_path_list.append(origin_img_path)
    base_path_list.append(detect_img_path)

    try:
        crop_path_list = load_crop_imgs_path(load_df_report,idx)
    except:
        pass

    return base_path_list, crop_path_list

def get_base_pics(base_path_list):
    pic_base = []
    for img_path in base_path_list:
        pic = base64.b64encode(open(img_path, 'rb').read()).decode()
        pic_base.append(pic)

    return pic_base

def get_crop_pics(crop_path_list):
    pic_crops = []
    try:
        for img_path in crop_path_list:
            pic = base64.b64encode(open(img_path, 'rb').read()).decode()
            pic_crops.append(pic)
    except:
        pass

    return pic_crops

def get_crop_htmls(df, idx, crop_path_list, pic_crops):
    htmls = []
    for i in range(len(crop_path_list)):
        if eval(df.loc[idx]['Crop_classes'])[i] == 'frame':
            category = eval(df.loc[idx]['Category'])[i]
            categories = {-1:'초기화', 0:'프레임', 1:'합법(공익)', 2:'정치', 3:'기타'}
            texts = eval(df.loc[idx]['ClovaOCR_text'])[i]
            basis = eval(df.loc[idx]['Category_basis'])[i]

            # 이미지 옆에 표 형태로 세부내용 넣기
            html = f"""
            <tr>
                <tr>
                    <td>
                    <table id="image">
                        <tr>
                            <td><img src="data:image/jpeg;base64,{pic_crops[i]}" width=200 height=100></td>
                        </tr>
                        <tr>
                            <td align=center border=1>frame</td>
                        </tr>
                    </table>
                    </td>
                    <td>    
                    <table border width=650 height=95%>
                        <tr><td align=center width=40>범례</td><td>{categories[category]}</td></tr>
                        <tr><td align=center width=40>내용</td><td class=visible>{texts}</td></tr>
                        <tr><td align=center width=40>근거</td><td class=visible>{basis}</td></tr>
                    </table>
                    </td>                    
                </tr>
            </tr>
            """
            htmls.append(html)
        else:
            category = eval(df.loc[idx]['Category'])[i]
            categories = {-1:'초기화', 0:'프레임', 1:'합법(공익)', 2:'정치', 3:'기타'}
            texts = eval(df.loc[idx]['ClovaOCR_text'])[i]
            basis = eval(df.loc[idx]['Category_basis'])[i]

            # 이미지 옆에 표 형태로 세부내용 넣기
            html = f"""
            <tr>
                <tr>
                    <td>
                    <table id="image">
                        <tr>
                            <td><img src="data:image/jpeg;base64,{pic_crops[i]}" width=200 height=100></td>
                        </tr>
                        <tr>
                            <td align=center border=1>crop_img_{i}</td>
                        </tr>
                    </table>
                    </td>
                    <td>    
                    <table border width=650 height=95%>
                        <tr><td align=center width=40>범례</td><td>{categories[category]}</td></tr>
                        <tr><td align=center width=40>내용</td><td class=visible>{texts}</td></tr>
                        <tr><td align=center width=40>근거</td><td class=visible>{basis}</td></tr>
                    </table>
                    </td>                    
                </tr>
            </tr>
            """
            htmls.append(html)

    return htmls

def get_folium_popups(df, idx):
    base_path_list, crop_path_list = load_imgs_path(df, idx)
    pic_base = get_base_pics(base_path_list)
    pic_crops = get_crop_pics(crop_path_list)

    base_h = len(pic_base) * 135
    crop_h = len(eval(df.loc[idx]['Crop_classes'])) * 135  # 만약 banner나 frame을 detect하지 못했다면 popup창의 크기를 조절

    crop_html = f''
    try:
        htmls = get_crop_htmls(df, idx, crop_path_list, pic_crops)
        if htmls != []:
            for i in range(len(htmls)):
                crop_html += htmls[i] + '\n'
    except:
        pass

    # 원본 이미지와 detect 이미지는 고정적으로 들어감
    image_tag = f"""
    <head>
    <meta charset="euc-kr">
    <link rel="stylesheet" href="">
    <style src="">
    </style>
    </head>
    <body>
        <div>
        <table class="table table-hover" border>
            <tr align=center>
                <th width="200">이미지</th>
                <th width="650">내용</th>
            </tr>
            <tr>
                <td>
                <table id="image">
                    <tr>
                        <td><img src="data:image/jpeg;base64,{pic_base[0]}" width=200 height=100></td>
                    </tr>
                    <tr>
                        <td align=center border=1>Origin Image</td>
                    </tr>
                </table>
                </td><td align=center>원본 이미지</td>
            </tr>
            <tr>
                <td>
                <table id="image">
                    <tr>
                        <td><img src="data:image/jpeg;base64,{pic_base[1]}" width=200 height=100></td>
                    </tr>
                    <tr>
                        <td align=center border=1>Detect Image</td>
                    </tr>
                </table>
                </td><td align=center>Yolo로 Detect한 이미지</td>
            </tr>
    """ + crop_html + """
    </body>
    """

    height = 59 + base_h + crop_h
    if height > 500:
        height = 500

    iframe = branca.element.IFrame(image_tag, width=902, height=height)
    popup = folium.Popup(iframe)

    return popup