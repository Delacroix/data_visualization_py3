import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                           'gy', 'pe', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
