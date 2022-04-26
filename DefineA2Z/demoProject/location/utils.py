import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from project.settings import BASE_DIR
from .models import Country,Location,District



area_mapping = {
    'adm0_en': 'ADM0_EN',
    'adm0_pcode': 'ADM0_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_pcode': 'ADM1_PCODE',
    'adm2_en': 'ADM2_EN',
    'adm2_pcode': 'ADM2_PCODE',
    'adm3_en': 'ADM3_EN',
    'adm3_pcode': 'ADM3_PCODE',
    'adm4_en': 'ADM4_EN',
    'adm4_pcode': 'ADM4_PCODE',
    'adm4_ref': 'ADM4_REF',
    'adm4alt1en': 'ADM4ALT1EN',
    'adm4alt2en': 'ADM4ALT2EN',
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'geom': 'MULTIPOINT',
}

country_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}
area_shp = os.path.abspath(os.path.join(BASE_DIR,'data/bgd_adm_bbs_20201113_SHP/bgd_admbndp_admALL_bbs_itos_20201113.shp'))
country_shp = os.path.abspath(os.path.join(BASE_DIR,'data/TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp'))


# def run(verbose=True):
#     lm = LayerMapping(Country, country_shp, country_mapping, transform=False, encoding='iso-8859-1')
#     lm.save(strict=True, verbose=True)


# def run(verbose=True):
#     lm = LayerMapping(Country, country_shp, country_mapping, transform=False)
#     lm.save(strict=True, verbose=verbose)


def run(verbose=True):
    lm = LayerMapping(Country, country_shp, country_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
