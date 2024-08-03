from flask import Flask, render_template
import pandas as pd
import folium
from folium.plugins import MarkerCluster,Fullscreen,HeatMapWithTime,HeatMap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('opencell.html')

@app.route('/map/<view>')
def create_map(view):
    m = folium.Map(location=[22.9734, 78.6569], zoom_start=4.5,control_scale=True) # start view
    Fullscreen(position='bottomright').add_to(m)
    marker_cluster = MarkerCluster().add_to(m)   # mark cluster object
    if view=="all_operators":
        df = pd.read_csv('india.csv')
        def color_for_operator(operator):
            if operator == "Airtel":
                return "red"
            elif operator == "Reliance Jio":
                return "blue"
            else:
                return "black"  # Default color
        for index, row in df.iterrows():
            operator = row['operator']
            city_n=row['city_name']
            coordinates = [row['latitude'], row['longitude']]
            color = color_for_operator(operator)
        
            folium.Marker(
                location=coordinates,
                icon=folium.Icon(color=color),
                popup=folium.Popup(f"Operator: {operator}<br>City: {city_n}", max_width=300)
            ).add_to(marker_cluster)
    elif view=="airtel":
        df = pd.read_csv('Airtel.csv')
        for index, row in df.iterrows():
            city_n=row['city_name']
            coordinates = [row['latitude'], row['longitude']]
            color = "red"
            folium.Marker(
                location=coordinates,
                icon=folium.Icon(color=color),
                popup=folium.Popup(f"City: {city_n}", max_width=300)
            ).add_to(marker_cluster)
    elif view=="jio":
        df = pd.read_csv('Jio.csv')
        for index, row in df.iterrows():
            city_n=row['city_name']
            coordinates = [row['latitude'], row['longitude']]
            color = "blue"
            folium.Marker(
                location=coordinates,
                icon=folium.Icon(color=color),
                popup=folium.Popup(f"City: {city_n}", max_width=300)
            ).add_to(marker_cluster)
    elif view=="vodafone":
        df = pd.read_csv('Vodafone.csv')
        for index, row in df.iterrows():
            city_n=row['city_name']
            coordinates = [row['latitude'], row['longitude']]
            color = "black"
            folium.Marker(
                location=coordinates,
                icon=folium.Icon(color=color),
                popup=folium.Popup(f"City: {city_n}", max_width=300)
            ).add_to(marker_cluster)
    elif view=="airtel_heatmap":
        heatmap_data = []
        df = pd.read_csv('Airtel.csv')
        for index, row in df.iterrows():
            coordinates = [row['latitude'], row['longitude']]
            heatmap_data.append(coordinates)
        HeatMap(heatmap_data).add_to(m)    
    else:
        heatmap_data = []
        df = pd.read_csv('Jio.csv')
        for index, row in df.iterrows():
            coordinates = [row['latitude'], row['longitude']]
            heatmap_data.append(coordinates)
        HeatMap(heatmap_data).add_to(m)    

    map_html = m._repr_html_()
    return map_html        


if __name__ == '__main__':
    app.run(debug=True, port=7001)



