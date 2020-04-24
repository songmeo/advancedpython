import pandas as pd
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def main():
	#merge tables
    A = pd.read_csv('otselennud.csv',sep=";")
    B = pd.read_csv('airports.dat',skiprows=1,names=['ID','Name','City','Country','IATA','ICAO','Latitude','Longitude','Altitude','Timezone','DST','DZ','Type','Source'])
    table = A.merge(B, left_on='IATA', right_on='IATA')
	
	#draw the map
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-20, 45, 24, 71], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)
    
    #add destination
    for row in table.itertuples():
        plt.plot([row.Longitude, 24.832799911499997], [row.Latitude, 59.41329956049999], color='blue', linewidth=1, marker='o', transform=ccrs.Geodetic())
        plt.text(row.Longitude, row.Latitude, row.IATA, fontsize=6, horizontalalignment='right', transform=ccrs.Geodetic())
    plt.title('Tallinna lennujaama lennud 2020', fontsize=10)
    plt.show()
	
if __name__ == '__main__':
    main()
