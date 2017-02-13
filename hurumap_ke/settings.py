import os
from collections import OrderedDict
import dj_database_url

# pull in the default wazimap settings
from wazimap.settings import *  # noqa


# insert our overrides before both census and wazimap
INSTALLED_APPS = ['hurumap_ke'] + INSTALLED_APPS


DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://wazimap:wazimap@localhost/wazimap')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL)
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Localise this instance of Wazimap
WAZIMAP['name'] = 'HURUmap Kenya'
WAZIMAP['url'] = 'http://kenya.hurumap.org'
WAZIMAP['country_code'] = 'KE'
WAZIMAP['country_name'] = 'Kenya'
WAZIMAP['country_profile'] = 'country-KE-Kenya'
WAZIMAP['profile_builder'] = 'hurumap_ke.profiles.get_census_profile'
WAZIMAP['levels'] = {
    'country': {
        'plural': 'countries',
        'children': ['county'],
    },
    'county': {
        'plural': 'counties',
    }
}
WAZIMAP['comparative_levels'] = ['country']
WAZIMAP['geometry_data'] = {
    'country': 'geo/country.topojson',
    'county': 'geo/county.topojson',
}

WAZIMAP['ga_tracking_id'] = 'UA-44795600-8'
WAZIMAP['twitter'] = '@Code4Africa'

WAZIMAP['map_centre'] = [0.3051933453207569, 37.908818734483155]
WAZIMAP['map_zoom'] = 6

WAZIMAP['topics'] = OrderedDict()

WAZIMAP['topics']['census'] = {
        'topic': 'census',
        'name': 'census 2009',
        'icon': '/static/img/census.png',
        'order': 1,
        'desc': 'Census data collected in 2009 provided by the Kenya National Bureau of Statistics',
        'profiles': [
            'Demographics',
            'Voter registration',
            'Households',
            'Protests',
            'School fires',
            'Crime report',
            'Employment',
        ]
    }

WAZIMAP['topics']['education'] = {
    'topic': 'education',
    'name': 'education',
    'icon': '/static/img/education.png',
    'desc': 'Education data from Twaweza',
    'profiles': [
        'Education',
    ]
}

WAZIMAP['topics']['health'] = {
        'topic': 'health',
        'name': 'health',
        'icon': '/static/img/health.png',
        'order': 2,
        'desc': 'Health data collected in 2014 by the Kenya National Bureau of Statistics ',
        'profiles': [
            'Contraceptive use',
            'Maternal care indicators',
            'Knowledge of HIV prevention methods',
            'ITN',
            'Fertility',
            'Vaccinations',
            'Type treatment',
            'Nutrition',
            'Health ratios'
        ]
     }
WAZIMAP['topics']['development'] = {
        'topic': 'development',
        'name': 'development',
        'icon': '/static/img/development.png',
        'order': 3,
        'desc': 'Crop production and Livestock population for the year 2014 provided by the Ministry of Agriculture, Livestock and Fisheries.',
        'profiles': [
            'Crop production',
            'Livestock'
        ],
    }

