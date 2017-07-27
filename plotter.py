from matplotlib import cm
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from matplotlib import rcParams
from matplotlib.pyplot import rc
import matplotlib.ticker as mtick
import numpy as np

#Set matplotlib parameters to be able to use Greek letters in plots
rcParams['text.usetex'] = True
rc('text.latex', preamble=r'\usepackage{amsmath}')
rcParams['axes.labelsize'] = 20
rcParams['axes.titlesize'] = 30
rcParams['xtick.labelsize'] =14
rcParams['ytick.labelsize'] =14
rcParams['xtick.major.size'] = 6
rcParams['ytick.major.size'] = 6


def state_extent(name):
    #For plotting a single state at a time... I haven't gone through every state yet
    #Returns latitude, longitude to be around state of interest
    if name =='AL':
        return [-89.0, -84.5, 29.0, 35.4]
    elif name == 'AZ':
        return [-115.7, -108.5, 30.0, 35.7]
    elif name == 'AR':
        return [-95.43, -89.37, 32.78, 35.2]
    elif name == 'CA':
        return [-125.3, -113.7, 32.0, 40.0]
    elif name == 'CO':
        return [-110.0, -101.3, 36.14, 41.36]
    elif name == 'CT':
        return [-74.12, -71.47, 38.8, 39.9]
    elif name == 'DE':
        return [-76.0, -75.0, 36.6, 38.0]
    elif name == 'FL':
        return [-88.0,-79., 23., 31.]
    elif name == 'GA':
        return [-86.1, -80.44, 30.06, 34.0]
    elif name == 'HI':
        return [-162.0, -152., 18.,23.]
    elif name == 'ID':
        return [-118.0, -110.5, 39.2, 45.7]
    elif name == 'IL':
        return [-92.24, -86.91, 36.74, 40.4]
    elif name == 'IN':
        return [-88.43, -84.53, 35.9, 41.95]
    elif name == 'IA':
        return [-96.98, -89.8, 40.14, 43.87]
    elif name == 'KS':
        return [-102.8, -94.2, 35.04, 38.3]
    elif name == 'NC':
        return [-85.0,-74., 32.,36.]
    elif name == 'PA':
        return [-81.0, -74., 37., 40.]
    else:
        return [-150, -70, 20, 45]
    """
    elif name == 'RI':
    elif name == 'SC':
    elif name == 'SD':
    elif name == 'TN':
    elif name == 'TX':
    elif name == 'UT':
    elif name == 'VT':
    elif name == 'VA':
    elif name == 'WA':
    elif name == 'WV':
    elif name == 'WI':
    elif name == 'WY':
    elif name == 'ND':
    elif name == 'OH':
    elif name == 'OK':
    elif name == 'OR':
    elif name == 'KY':
    elif name == 'LA':
    elif name == 'ME':
    elif name == 'MD':
    elif name == 'MA':
    elif name == 'MI':
    elif name == 'MN':
    elif name == 'MS':
    elif name == 'MO':
    elif name == 'MT':
    elif name == 'NE':
    elif name == 'NV':
    elif name == 'NH':
    elif name == 'NJ':
    elif name == 'NM':
    elif name == 'NY':
    """
        
def state_plot_data_model(dataseries1, dataseries2, name, data_min, data_max, vmin, vmax, plt_title, cb2_label, use_cmap = cm.seismic):
    fig = plt.figure(figsize=(14.0, 7.0))
    ax1 = plt.axes([0.0, 0.0, 0.45, 1.0],projection=ccrs.Miller(), aspect=1.3)
    ax2 = plt.axes([0.45, 0.0, 0.45, 1.0],projection=ccrs.Miller(), aspect=1.3)
    ax1.set_extent(state_extent(name))
    ax2.set_extent(state_extent(name))
    
    filename = 'cb_2015_us_county_5m/cb_2015_us_county_5m.shp'
    states_codes={'AL':'01','AZ':'04','AR':'05','CA':'06','CO':'08','CT':'09','DE':'10','FL':'12','GA':'13','HI':'15','ID':'16','IL':'17','IN':'18','IA':'19','KS':'20','KY':'21','LA':'22','ME':'23','MD':'24','MA':'25','MI':'26','MN':'27','MS':'28','MO':'29','MT':'30','NE':'31','NV':'32','NH':'33','NJ':'34','NM':'35','NY':'36','NC':'37','ND':'38','OH':'39','OK':'40','OR':'41','PA':'42','RI':'44','SC':'45','SD':'46','TN':'47','TX':'48','UT':'49','VT':'50','VA':'51','WA':'53','WV':'54','WI':'55','WY':'56'}
    
    the_lw = 0.0
    for state, record in zip(shpreader.Reader(filename).geometries(), shpreader.Reader(filename).records()):
        id = int(record.__dict__['attributes']['GEOID'])
        if id>int(states_codes[name])*1000 and id<(1+int(states_codes[name]))*1000:
            if id in dataseries1.index:
                value = (dataseries1.loc[id]-data_min)/(data_max-data_min)
                facecolor = use_cmap(value)
                edgecolor = 'black'
                #Is the county in Hawaii, Alaska, or the mainland?
                ax1.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
            else:
                facecolor = 'gray'
                edgecolor = 'black'
                #Is the county in Hawaii, Alaska, or the mainland?
                ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw) 
            
            if id in dataseries2.index:
                value = (dataseries2.loc[id]-data_min)/(data_max-data_min)
                facecolor = use_cmap(value)
                edgecolor = 'black'
                #Is the county in Hawaii, Alaska, or the mainland?
                ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
            else:
                facecolor = 'gray'
                edgecolor = 'black'
                #Is the county in Hawaii, Alaska, or the mainland?
                ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw) 
    
    filename = 'cb_2015_us_state_5m/cb_2015_us_state_5m.shp'  
    the_lw = 0.5
    for state, record in zip(shpreader.Reader(filename).geometries(), shpreader.Reader(filename).records()):
        id = int(record.__dict__['attributes']['GEOID'])
        if int(id)==int(states_codes[name]):
            facecolor = use_cmap(0.0)
            edgecolor = 'black'
            #Is the county in Hawaii, Alaska, or the mainland?
            ax1.add_geometries(state, crs=ccrs.Miller(), facecolor='none', alpha=1.0, edgecolor=edgecolor, linewidth=the_lw)
            ax2.add_geometries(state, crs=ccrs.Miller(), facecolor='none', alpha=1.0, edgecolor=edgecolor, linewidth=the_lw)
        
    print "Plotting..."
    ax1.background_patch.set_visible(False)
    ax1.outline_patch.set_visible(False)
    ax2.background_patch.set_visible(False)
    ax2.outline_patch.set_visible(False)
    
    ax1.set_title('Data')
    ax2.set_title('Model')
    cbar_step=(vmax-vmin)/5
    
    axc2 = plt.axes([0.92, 0.25, 0.02, 0.5], frameon=False)
    norm2 = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cb2 = mpl.colorbar.ColorbarBase(axc2, cmap=use_cmap,norm=norm2,orientation='vertical')
    cb2.ax.set_yticklabels(['{:.0f}\%'.format(x) for x in np.arange(vmin, vmax+cbar_step, cbar_step)])    
    cb2.set_label(cb2_label)
    
    plt.savefig('plots/'+str(plt_title)+'.pdf',bbox_inches='tight')
    #plt.show()
    return 0


#Define plotting function, so we can see the results in a nice way
def national_plot(dataseries, data_min, data_max, vmin, vmax, plt_title,colorbar_label, use_cmap = cm.seismic, AK_value = False):
    fig = plt.figure(figsize=(14.0,6.3))
    #Mainland
    ax = plt.axes([0.25,0,0.75,1],projection=ccrs.Miller(), aspect=1.3, frameon=False)
    ax.set_extent([-127.0,-65., 23.,43.])
    #Alaska
    ax2 = plt.axes([0,0.3,0.27,0.6],projection=ccrs.Miller(), aspect=1.7, frameon=False)
    ax2.set_extent([-180.0,-132., 47.,62.])
    #Hawaii
    ax3 = plt.axes([0.1, 0.05,0.2,0.3],projection=ccrs.Miller(), aspect=1.3, frameon=False)
    ax3.set_extent([-162.0,-152., 18.,23.])
    filename = 'cb_2015_us_county_5m/cb_2015_us_county_5m.shp'
    the_lw = 0.0
    
    for state, record in zip(shpreader.Reader(filename).geometries(), shpreader.Reader(filename).records()):
        id = int(record.__dict__['attributes']['GEOID'])
        if id == '46102':
            id = '46113'
        if id in dataseries.index:
            value = (dataseries.loc[id]-data_min)/(data_max-data_min)
            facecolor = use_cmap(value)
            edgecolor = 'black'
            #Is the county in Hawaii, Alaska, or the mainland?
            if int(record.__dict__['attributes']['GEOID'])<2991 and int(record.__dict__['attributes']['GEOID'])>2013: 
                ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
            elif int(record.__dict__['attributes']['GEOID'])<15010 and int(record.__dict__['attributes']['GEOID'])>15000: 
                ax3.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
            else:
                ax.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
        else:
            facecolor = 'gray'
            edgecolor = 'black'
            #Is the county in Hawaii, Alaska, or the mainland?
            if int(record.__dict__['attributes']['GEOID'])<2991 and int(record.__dict__['attributes']['GEOID'])>2013: 
                if AK_value:
                    ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=cm.seismic(AK_value), edgecolor=edgecolor, linewidth=the_lw)
                else:
                    ax2.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
                    
            elif int(record.__dict__['attributes']['GEOID'])<15010 and int(record.__dict__['attributes']['GEOID'])>15000: 
                ax3.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
            else:
                ax.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw) 
    
    filename = 'cb_2015_us_state_5m/cb_2015_us_state_5m.shp'  
    the_lw = 0.5
    for state, record in zip(shpreader.Reader(filename).geometries(), shpreader.Reader(filename).records()):
        id = int(record.__dict__['attributes']['GEOID'])
        facecolor = use_cmap(0.0)
        edgecolor = 'black'
        #Is the county in Hawaii, Alaska, or the mainland?
        if int(record.__dict__['attributes']['GEOID'])==2: 
            ax2.add_geometries(state, crs=ccrs.Miller(), facecolor='none', alpha=1.0, edgecolor=edgecolor, linewidth=the_lw)
        elif int(record.__dict__['attributes']['GEOID'])==15: 
            ax3.add_geometries(state, crs=ccrs.Miller(), facecolor='none', alpha=1.0, edgecolor=edgecolor, linewidth=the_lw)
        else:
            ax.add_geometries(state, crs=ccrs.Miller(), facecolor='none', alpha=1.0, edgecolor=edgecolor, linewidth=the_lw)
        
    print "Plotting..."
    ax.background_patch.set_visible(False)
    ax.outline_patch.set_visible(False)
    ax2.background_patch.set_visible(False)
    ax2.outline_patch.set_visible(False)
    ax3.background_patch.set_visible(False)
    ax3.outline_patch.set_visible(False)

    #Add colorbar
    axc = plt.axes([0.93, 0.1, 0.02, 0.5], frameon=False)
    cmap = use_cmap
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cb = mpl.colorbar.ColorbarBase(axc, cmap=cmap,norm=norm,orientation='vertical')
    cbar_step=(vmax-vmin)/8
    print ['{:.0f}\%'.format(x) for x in np.arange(vmin, vmax+cbar_step, cbar_step)]
    cb.ax.set_yticklabels(['{:.0f}\%'.format(x) for x in np.arange(vmin, vmax+cbar_step, cbar_step)])
    cb.set_label(colorbar_label)
    
    plt.savefig('plots/'+str(plt_title)+'.pdf',bbox_inches='tight')
    #plt.show()
    return 0
    
#Define plotting function, so we can see the results in a nice way
def state_plot(dataseries,name, data_min, data_max, vmin, vmax, plt_title,colorbar_label, use_cmap = cm.seismic, AK_value = False):
    fig = plt.figure(figsize=(10.0,10.0))
    ax = plt.axes(projection=ccrs.Miller(), aspect=1.3)
    ax.set_extent(state_extent(name))
    
    filename = 'cb_2015_us_county_5m/cb_2015_us_county_5m.shp'
    the_lw = 0.1
    for state, record in zip(shpreader.Reader(filename).geometries(), shpreader.Reader(filename).records()):
        id = int(record.__dict__['attributes']['GEOID'])
        if id == '46102':
            id = '46113'
        if id in dataseries.index:
            value = (dataseries.loc[id]-data_min)/(data_max-data_min)
            facecolor = use_cmap(value)
            edgecolor = 'black'
            ax.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)
        else:
            facecolor = 'gray'
            edgecolor = 'black'
            ax.add_geometries(state, crs=ccrs.Miller(), facecolor=facecolor, edgecolor=edgecolor, linewidth=the_lw)                    
    print "Plotting..."
    ax.background_patch.set_visible(False)
    ax.outline_patch.set_visible(False)

    #Add colorbar
    axc = plt.axes([0.93, 0.1, 0.02, 0.5], frameon=False)
    cmap = use_cmap
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cb = mpl.colorbar.ColorbarBase(axc, cmap=cmap,norm=norm,orientation='vertical')
    cb.set_label(colorbar_label)
    
    plt.savefig('plots/'+str(plt_title)+'.pdf',bbox_inches='tight')
    #plt.show()
    return 0