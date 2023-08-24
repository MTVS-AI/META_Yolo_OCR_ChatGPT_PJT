from flask import Blueprint, render_template
import pandas as pd
import folium
import folium.plugins
from ban.modules import modules
import os
from tqdm import tqdm

bp = Blueprint('main', __name__, url_prefix='/')

dir_path = 'folium/'
os.makedirs(dir_path, exist_ok=True)

# csv 파일에서 가져옴
df = pd.read_csv('ban/reports/report_2023_08_12/report_2023_08_12.csv')
locations = ['[37.395394, 127.109329]', '[37.394178, 127.109384]', '[37.392718, 127.109348]', '[37.391850, 127.112509]',
             '[37.393454, 127.112579]', '[37.395544, 127.112627]', '[37.396501, 127.111183]', '[37.396499, 127.113374]',
             '[37.396010, 127.115203]', '[37.394405, 127.116533]', '[37.393466, 127.118316]', '[37.390801, 127.117001]',
             '[37.391880, 127.119013]', '[37.394036, 127.106956]', '[37.396431, 127.108427]', '[37.397943, 127.110214]']
df['Location'] = locations

@bp.route('/')
def index_main():
    return render_template('index.html')

@bp.route('/map')
def map_main():
    center = eval(df.iloc[0]['Location'])
    map = folium.Map(location=center, min_lon=124.36, min_lat=38.61, max_lon=131.52, max_lat=33.11, control_scale=True,
                     max_bounds=True, min_zoom=15, zoom_start=16)

    political_group = folium.FeatureGroup(name="정치").add_to(map)
    illegal_group = folium.FeatureGroup(name="불법").add_to(map)
    legal_group = folium.FeatureGroup(name="합법").add_to(map)

    folium.LayerControl(collapsed=False).add_to(map)

    for i in tqdm(range(len(df))):
        popup = modules.get_folium_popups(df, i)

        if 2 in eval(df.iloc[i]['Category']):
            political_group.add_child(
                folium.Marker(location=eval(df.iloc[i]['Location']), icon=folium.Icon(color='blue', icon='bookmark'),
                              popup=popup))
        elif 3 in eval(df.iloc[i]['Category']):
            illegal_group.add_child(
                folium.Marker(location=eval(df.iloc[i]['Location']), icon=folium.Icon(color='red', icon='star'),
                              popup=popup))
        else:
            legal_group.add_child(
                folium.Marker(location=eval(df.iloc[i]['Location']), icon=folium.Icon(color='green', icon='check'),
                              popup=popup))

    map.save('ban/templates/map.html')

    return map.get_root().render()