from flask import Flask, render_template
import geopandas as gpd
import folium

app = Flask(__name__)

@app.route('/')
def index():
    gdf = gpd.read_file('data/zinke_soil.shp')
    
    # Создание карты
    m = folium.Map(location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=10)

    # Добавление данных на карту
    folium.GeoJson(gdf).add_to(m)

    # Сохранение карты в HTML
    m.save('templates/zinke_soil_map.html')
    
    return render_template('zinke_soil_map.html')

if __name__ == '__main__':
    app.run(debug=True)
