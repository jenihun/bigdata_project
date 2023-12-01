from flask import Flask, render_template
import folium
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    
    #중심 좌표 설정
    center_coordinates = [37.5665, 126.9780]
    
    # Folium 지도 생성
    m = folium.Map(location=center_coordinates, zoom_start=5)

    # 마커 추가
    marker = folium.Marker(location=[37.5665, 126.9780], popup='<strong>서울</strong>', tooltip='Click me!')
    marker.add_to(m)

    # Folium 맵을 HTML로 변환하여 전달
    map_html = m._repr_html_()

    # 레이더 차트 데이터 및 코드
    # 예시 데이터
    labels = ['A', 'B', 'C', 'D', 'E']
    data = [5, 3, 7, 2, 8]

    # 레이더 차트 그리기
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(labels + [labels[0]], data + [data[0]], color='blue', linewidth=2, linestyle='solid')
    ax.fill(labels + [labels[0]], data + [data[0]], color='blue', alpha=0.4)

    # 차트를 base64로 인코딩하여 HTML로 전달
    buf = BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buf)
    buf.seek(0)
    plt.close(fig)
    chart_data = base64.b64encode(buf.read()).decode('utf-8')

    return render_template('index.html', map_html=map_html, chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)