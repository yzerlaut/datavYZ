import sys, os, platform
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir))

from datavyz.dependencies import *

"""
MANUSCRIPT ENVIRONMENT
"""
ENVIRONMENTS = {
    'manuscript': {
	'fontsize':8,
	'default_color':'k',
        'single_plot_size':(28., 20.), # mm
        'hspace_size':12., # mm
        'wspace_size':16., # mm
        'left_size':20., # mm
        'right_size':4., # mm
        'top_size':7., # mm
        'bottom_size':15., # mm
        'background':'w',
        'facecolor':'none',
        'transparency':True,
        'dpi':150,
        'size_factor': 1.,
        'markersize':3,
    }
}


# SCREEN ENVIRONMENT
# "screen" is just an expanded version of 
ENVIRONMENTS['screen'], screen_factor = {}, 1.5
for key, val in ENVIRONMENTS['manuscript'].items():
    if 'plot_size' in key:
        ENVIRONMENTS['screen'][key]=(screen_factor*val[0],screen_factor*val[1])
    elif 'size' in key:
        ENVIRONMENTS['screen'][key]=screen_factor*np.float(val)
    else:
        ENVIRONMENTS['screen'][key] = val
        
"""
NOTEBOOK ENVIRONMENT
"""
ENVIRONMENTS['notebook'] = {
	'fontsize':11,
	'default_color':'k',
        'single_plot_size':(28.*1.5, 20.*1.5), # mm
        'hspace_size':12.*1.5, # mm
        'wspace_size':16.*1.5, # mm
        'left_size':20*1.5, # mm
        'right_size':4.*1.5, # mm
        'top_size':7.*1.5, # mm
        'bottom_size':19.*1.5, # mm
        'background':'w',
        'facecolor':'none',
        'transparency':False,
        'dpi':200,
        'size_factor': 1.,
}
"""
DARK NOTEBOOK ENVIRONMENT
"""
# "screen" is just an expanded version of 
ENVIRONMENTS['dark_notebook'] = ENVIRONMENTS['notebook'].copy()
ENVIRONMENTS['dark_notebook']['facecolor'] = 'darkslategray'
ENVIRONMENTS['dark_notebook']['default_color'] = 'w'

"""
VISUAL STIMULATION ENVIRONMENT
"""
ENVIRONMENTS['visual_stim'] = {
	'fontsize':12,
	'default_color':'w',
        'single_plot_size':(200.*16./9., 200.), # mm
        'hspace_size':1., # mm
        'wspace_size':1., # mm
        'left_size':1., # mm
        'right_size':1., # mm
        'top_size':1., # mm
        'bottom_size':1., # mm
        'background':'dark',
        'facecolor':'dimgrey',
        'transparency':True,
        'dpi':150,
}

def set_env_variables(cls, key):

    for key, val in ENVIRONMENTS[key].items():
        setattr(cls, key, val)

    for k, val in ENVIRONMENTS['manuscript'].items():
        if k not in dir(cls):
            setattr(cls, k, val)
        
    
def update_rcParams(cls):
    mpl.rcParams.update({'axes.labelsize': cls.fontsize,
                         'axes.titlesize': cls.fontsize,
                         'figure.titlesize': cls.fontsize,
                         'font.size': cls.fontsize,
                         'legend.fontsize': cls.fontsize,
                         'xtick.labelsize': cls.fontsize,
                         'ytick.labelsize': cls.fontsize,
                         'figure.facecolor': cls.facecolor,
                         'legend.facecolor': cls.facecolor,
                         'axes.facecolor': cls.facecolor,
                         'savefig.transparent':cls.transparency,
                         'savefig.dpi':cls.dpi,
                         'savefig.facecolor': cls.facecolor})
    
if __name__=='__main__':

    import sys, os
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))
                    
    import numpy as np
    
    from main import graph_env
    for key in ENVIRONMENTS:
        ge = graph_env(key)
        ge.scatter(np.random.randn(100), np.random.randn(100))
        ge.title(plt.gca(), key)
        ge.show()
