import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")

map=folium.Map(location=[38,-99],zoom_start=6,tiles="Mapbox Bright")

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if (elevation<1000):
        return 'green'
    elif (1000<=elevation<3000):
        return 'orange'
    else:
        return 'red'

fg=folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m", fill_color=color_producer(el), color='grey', fill_opacity=0.7, fill=True))
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))
map.add_child(fg)
map.save("Map1.html")
