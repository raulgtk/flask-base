# coding: utf-8

from lib.geo import Country

country_list = []

countries = {
    'AF': {'iso3': 'AFG', 'number': '004', 'name': u'Afganistán'},
    'AX': {'iso3': 'ALA', 'number': '248', 'name': u'Aland'},
    'AL': {'iso3': 'ALB', 'number': '008', 'name': u'Albania'},
    'DE': {'iso3': 'DEU', 'number': '276', 'name': u'Alemania'},
    'AD': {'iso3': 'AND', 'number': '020', 'name': u'Andorra'},
    'AO': {'iso3': 'AGO', 'number': '024', 'name': u'Angola'},
    'AI': {'iso3': 'AIA', 'number': '660', 'name': u'Anguila'},
    'AG': {'iso3': 'ATG', 'number': '028', 'name': u'Antigua y Barbuda'},
    'AN': {'iso3': 'ANT', 'number': '530', 'name': u'Antillas Neerlandesas'},
    'SA': {'iso3': 'SAU', 'number': '682', 'name': u'Arabia Saudita'},
    'DZ': {'iso3': 'DZA', 'number': '012', 'name': u'Argelia'},
    'AR': {'iso3': 'ARG', 'number': '032', 'name': u'Argentina'},
    'AM': {'iso3': 'ARM', 'number': '051', 'name': u'Armenia'},
    'AW': {'iso3': 'ABW', 'number': '533', 'name': u'Aruba'},
    'AU': {'iso3': 'AUS', 'number': '036', 'name': u'Australia'},
    'AT': {'iso3': 'AUT', 'number': '040', 'name': u'Austria'},
    'AZ': {'iso3': 'AZE', 'number': '031', 'name': u'Azerbaiyán'},
    'BS': {'iso3': 'BHS', 'number': '044', 'name': u'Bahamas'},
    'BH': {'iso3': 'BHR', 'number': '048', 'name': u'Baréin'},
    'BD': {'iso3': 'BGD', 'number': '050', 'name': u'Bangladés'},
    'BB': {'iso3': 'BRB', 'number': '052', 'name': u'Barbados'},
    'BE': {'iso3': 'BEL', 'number': '056', 'name': u'Bélgica'},
    'BZ': {'iso3': 'BLZ', 'number': '084', 'name': u'Belice'},
    'BJ': {'iso3': 'BEN', 'number': '204', 'name': u'Benín'},
    'BM': {'iso3': 'BMU', 'number': '060', 'name': u'Bermudas'},
    'BY': {'iso3': 'BLR', 'number': '112', 'name': u'Bielorrusia'},
    'MM': {'iso3': 'MMR', 'number': '104', 'name': u'Birmania'},
    'BO': {'iso3': 'BOL', 'number': '068', 'name': u'Bolivia'},
    'BA': {'iso3': 'BIH', 'number': '070', 'name': u'Bosnia y Herzegovina'},
    'BW': {'iso3': 'BWA', 'number': '072', 'name': u'Botsuana'},
    'BV': {'iso3': 'BVT', 'number': '074', 'name': u'Isla Bouvet'},
    'BR': {'iso3': 'BRA', 'number': '076', 'name': u'Brasil'},
    'BN': {'iso3': 'BRN', 'number': '096', 'name': u'Brunéi'},
    'BG': {'iso3': 'BGR', 'number': '100', 'name': u'Bulgaria'},
    'BF': {'iso3': 'BFA', 'number': '854', 'name': u'Burkina Faso'},
    'BI': {'iso3': 'BDI', 'number': '108', 'name': u'Burundi'},
    'BT': {'iso3': 'BTN', 'number': '064', 'name': u'Bután'},
    'CV': {'iso3': 'CPV', 'number': '132', 'name': u'Cabo Verde'},
    'KY': {'iso3': 'CYM', 'number': '136', 'name': u'Islas Caimán'},
    'KH': {'iso3': 'KHM', 'number': '116', 'name': u'Camboya'},
    'CM': {'iso3': 'CMR', 'number': '120', 'name': u'Camerún'},
    'CA': {'iso3': 'CAN', 'number': '124', 'name': u'Canadá'},
    'CF': {'iso3': 'CAF', 'number': '140', 'name': u'República Centroafricana'},
    'TD': {'iso3': 'TCD', 'number': '148', 'name': u'Chad'},
    'CZ': {'iso3': 'CZE', 'number': '203', 'name': u'República Checa'},
    'CL': {'iso3': 'CHL', 'number': '152', 'name': u'Chile'},
    'CN': {'iso3': 'CHN', 'number': '156', 'name': u'China'},
    'CY': {'iso3': 'CYP', 'number': '196', 'name': u'Chipre'},
    'CC': {'iso3': 'CCK', 'number': '166', 'name': u'Islas Cocos'},
    'CO': {'iso3': 'COL', 'number': '170', 'name': u'Colombia'},
    'KM': {'iso3': 'COM', 'number': '174', 'name': u'Comoras'},
    'CG': {'iso3': 'COG', 'number': '178', 'name': u'República del Congo'},
    'CD': {'iso3': 'COD', 'number': '180', 'name': u'Rep. Dem. del Congo'},
    'CK': {'iso3': 'COK', 'number': '184', 'name': u'Islas Cook'},
    'KP': {'iso3': 'PRK', 'number': '408', 'name': u'Corea del Norte'},
    'KR': {'iso3': 'KOR', 'number': '410', 'name': u'Corea del Sur'},
    'CI': {'iso3': 'CIV', 'number': '384', 'name': u'Costa de Marfil'},
    'CR': {'iso3': 'CRI', 'number': '188', 'name': u'Costa Rica'},
    'HR': {'iso3': 'HRV', 'number': '191', 'name': u'Croacia'},
    'CW': {'iso3': 'CUW', 'number': '531', 'name': u'Curazao'},
    'CU': {'iso3': 'CUB', 'number': '192', 'name': u'Cuba'},
    'DK': {'iso3': 'DNK', 'number': '208', 'name': u'Dinamarca'},
    'DM': {'iso3': 'DMA', 'number': '212', 'name': u'Dominica'},
    'DO': {'iso3': 'DOM', 'number': '214', 'name': u'República Dominicana'},
    'EC': {'iso3': 'ECU', 'number': '218', 'name': u'Ecuador'},
    'EG': {'iso3': 'EGY', 'number': '818', 'name': u'Egipto'},
    'SV': {'iso3': 'SLV', 'number': '222', 'name': u'El Salvador'},
    'AE': {'iso3': 'ARE', 'number': '784', 'name': u'Emiratos Árabes Unidos'},
    'ER': {'iso3': 'ERI', 'number': '232', 'name': u'Eritrea'},
    'SK': {'iso3': 'SVK', 'number': '703', 'name': u'Eslovaquia'},
    'SI': {'iso3': 'SVN', 'number': '705', 'name': u'Eslovenia'},
    'ES': {'iso3': 'ESP', 'number': '724', 'name': u'España'},
    'US': {'iso3': 'USA', 'number': '840', 'name': u'Estados Unidos'},
    'EE': {'iso3': 'EST', 'number': '233', 'name': u'Estonia'},
    'ET': {'iso3': 'ETH', 'number': '231', 'name': u'Etiopía'},
    'FO': {'iso3': 'FRO', 'number': '234', 'name': u'Islas Feroe'},
    'PH': {'iso3': 'PHL', 'number': '608', 'name': u'Filipinas'},
    'FI': {'iso3': 'FIN', 'number': '246', 'name': u'Finlandia'},
    'FJ': {'iso3': 'FJI', 'number': '242', 'name': u'Fiyi'},
    'FR': {'iso3': 'FRA', 'number': '250', 'name': u'Francia'},
    'GA': {'iso3': 'GAB', 'number': '266', 'name': u'Gabón'},
    'GM': {'iso3': 'GMB', 'number': '270', 'name': u'Gambia'},
    'GE': {'iso3': 'GEO', 'number': '268', 'name': u'Georgia'},
    'GS': {'iso3': 'SGS', 'number': '239', 'name': u'Islas Georgias del Sur y Sandwich del Sur'},
    'GH': {'iso3': 'GHA', 'number': '288', 'name': u'Ghana'},
    'GI': {'iso3': 'GIB', 'number': '292', 'name': u'Gibraltar'},
    'GD': {'iso3': 'GRD', 'number': '308', 'name': u'Granada'},
    'GR': {'iso3': 'GRC', 'number': '300', 'name': u'Grecia'},
    'GL': {'iso3': 'GRL', 'number': '304', 'name': u'Groenlandia'},
    'GP': {'iso3': 'GLP', 'number': '312', 'name': u'Guadalupe'},
    'GU': {'iso3': 'GUM', 'number': '316', 'name': u'Guam'},
    'GT': {'iso3': 'GTM', 'number': '320', 'name': u'Guatemala'},
    'GF': {'iso3': 'GUF', 'number': '254', 'name': u'Guayana Francesa'},
    'GG': {'iso3': 'GGY', 'number': '831', 'name': u'Guernsey'},
    'GN': {'iso3': 'GIN', 'number': '324', 'name': u'Guinea'},
    'GQ': {'iso3': 'GNQ', 'number': '226', 'name': u'Guinea Ecuatorial'},
    'GW': {'iso3': 'GNB', 'number': '624', 'name': u'Guinea-Bisáu'},
    'GY': {'iso3': 'GUY', 'number': '328', 'name': u'Guyana'},
    'HT': {'iso3': 'HTI', 'number': '332', 'name': u'Haití'},
    'HM': {'iso3': 'HMD', 'number': '334', 'name': u'Islas Heard y McDonald'},
    'HN': {'iso3': 'HND', 'number': '340', 'name': u'Honduras'},
    'HK': {'iso3': 'HKG', 'number': '344', 'name': u'Hong Kong'},
    'HU': {'iso3': 'HUN', 'number': '348', 'name': u'Hungría'},
    'IN': {'iso3': 'IND', 'number': '356', 'name': u'India'},
    'ID': {'iso3': 'IDN', 'number': '360', 'name': u'Indonesia'},
    'IR': {'iso3': 'IRN', 'number': '364', 'name': u'Irán'},
    'IQ': {'iso3': 'IRQ', 'number': '368', 'name': u'Irak'},
    'IE': {'iso3': 'IRL', 'number': '372', 'name': u'Irlanda'},
    'IS': {'iso3': 'ISL', 'number': '352', 'name': u'Islandia'},
    'IL': {'iso3': 'ISR', 'number': '376', 'name': u'Israel'},
    'IT': {'iso3': 'ITA', 'number': '380', 'name': u'Italia'},
    'JM': {'iso3': 'JAM', 'number': '388', 'name': u'Jamaica'},
    'JP': {'iso3': 'JPN', 'number': '392', 'name': u'Japón'},
    'JE': {'iso3': 'JEY', 'number': '832', 'name': u'Jersey'},
    'JO': {'iso3': 'JOR', 'number': '400', 'name': u'Jordania'},
    'KZ': {'iso3': 'KAZ', 'number': '398', 'name': u'Kazajistán'},
    'KE': {'iso3': 'KEN', 'number': '404', 'name': u'Kenia'},
    'KG': {'iso3': 'KGZ', 'number': '417', 'name': u'Kirguistán'},
    'KI': {'iso3': 'KIR', 'number': '296', 'name': u'Kiribati'},
    'KW': {'iso3': 'KWT', 'number': '414', 'name': u'Kuwait'},
    'LA': {'iso3': 'LAO', 'number': '418', 'name': u'Laos'},
    'LS': {'iso3': 'LSO', 'number': '426', 'name': u'Lesoto'},
    'LV': {'iso3': 'LVA', 'number': '428', 'name': u'Letonia'},
    'LB': {'iso3': 'LBN', 'number': '422', 'name': u'Líbano'},
    'LR': {'iso3': 'LBR', 'number': '430', 'name': u'Liberia'},
    'LY': {'iso3': 'LBY', 'number': '434', 'name': u'Libia'},
    'LI': {'iso3': 'LIE', 'number': '438', 'name': u'Liechtenstein'},
    'LT': {'iso3': 'LTU', 'number': '440', 'name': u'Lituania'},
    'LU': {'iso3': 'LUX', 'number': '442', 'name': u'Luxemburgo'},
    'MO': {'iso3': 'MAC', 'number': '446', 'name': u'Macao'},
    'MK': {'iso3': 'MKD', 'number': '807', 'name': u'República de Macedonia'},
    'MG': {'iso3': 'MDG', 'number': '450', 'name': u'Madagascar'},
    'MY': {'iso3': 'MYS', 'number': '458', 'name': u'Malasia'},
    'MW': {'iso3': 'MWI', 'number': '454', 'name': u'Malaui'},
    'MV': {'iso3': 'MDV', 'number': '462', 'name': u'Maldivas'},
    'ML': {'iso3': 'MLI', 'number': '466', 'name': u'Malí'},
    'MT': {'iso3': 'MLT', 'number': '470', 'name': u'Malta'},
    'FK': {'iso3': 'FLK', 'number': '238', 'name': u'Islas Malvinas'},
    'IM': {'iso3': 'IMN', 'number': '833', 'name': u'Isla de Man'},
    'MP': {'iso3': 'MNP', 'number': '580', 'name': u'Islas Marianas del Norte'},
    'MA': {'iso3': 'MAR', 'number': '504', 'name': u'Marruecos'},
    'MH': {'iso3': 'MHL', 'number': '584', 'name': u'Islas Marshall'},
    'MQ': {'iso3': 'MTQ', 'number': '474', 'name': u'Martinica'},
    'MU': {'iso3': 'MUS', 'number': '480', 'name': u'Mauricio'},
    'MR': {'iso3': 'MRT', 'number': '478', 'name': u'Mauritania'},
    'YT': {'iso3': 'MYT', 'number': '175', 'name': u'Mayotte'},
    'MX': {'iso3': 'MEX', 'number': '484', 'name': u'México'},
    'FM': {'iso3': 'FSM', 'number': '583', 'name': u'Micronesia'},
    'MD': {'iso3': 'MDA', 'number': '498', 'name': u'Moldavia'},
    'MC': {'iso3': 'MCO', 'number': '492', 'name': u'Mónaco'},
    'MN': {'iso3': 'MNG', 'number': '496', 'name': u'Mongolia'},
    'ME': {'iso3': 'MNE', 'number': '499', 'name': u'Montenegro'},
    'MS': {'iso3': 'MSR', 'number': '500', 'name': u'Montserrat'},
    'MZ': {'iso3': 'MOZ', 'number': '508', 'name': u'Mozambique'},
    'NA': {'iso3': 'NAM', 'number': '516', 'name': u'Namibia'},
    'NR': {'iso3': 'NRU', 'number': '520', 'name': u'Nauru'},
    'CX': {'iso3': 'CXR', 'number': '162', 'name': u'Isla de Navidad'},
    'NP': {'iso3': 'NPL', 'number': '524', 'name': u'Nepal'},
    'NI': {'iso3': 'NIC', 'number': '558', 'name': u'Nicaragua'},
    'NE': {'iso3': 'NER', 'number': '562', 'name': u'Níger'},
    'NG': {'iso3': 'NGA', 'number': '566', 'name': u'Nigeria'},
    'NU': {'iso3': 'NIU', 'number': '570', 'name': u'Niue'},
    'NF': {'iso3': 'NFK', 'number': '574', 'name': u'Norfolk'},
    'NO': {'iso3': 'NOR', 'number': '578', 'name': u'Noruega'},
    'NC': {'iso3': 'NCL', 'number': '540', 'name': u'Nueva Caledonia'},
    'NZ': {'iso3': 'NZL', 'number': '554', 'name': u'Nueva Zelanda'},
    'OM': {'iso3': 'OMN', 'number': '512', 'name': u'Omán'},
    'NL': {'iso3': 'NLD', 'number': '528', 'name': u'Países Bajos'},
    'PK': {'iso3': 'PAK', 'number': '586', 'name': u'Pakistán'},
    'PW': {'iso3': 'PLW', 'number': '585', 'name': u'Palaos'},
    'PS': {'iso3': 'PSE', 'number': '275', 'name': u'Estado de Palestina'},
    'PA': {'iso3': 'PAN', 'number': '591', 'name': u'Panamá'},
    'PG': {'iso3': 'PNG', 'number': '598', 'name': u'Papúa Nueva Guinea'},
    'PY': {'iso3': 'PRY', 'number': '600', 'name': u'Paraguay'},
    'PE': {'iso3': 'PER', 'number': '604', 'name': u'Perú'},
    'PN': {'iso3': 'PCN', 'number': '612', 'name': u'Islas Pitcairn'},
    'PF': {'iso3': 'PYF', 'number': '258', 'name': u'Polinesia Francesa'},
    'PL': {'iso3': 'POL', 'number': '616', 'name': u'Polonia'},
    'PT': {'iso3': 'PRT', 'number': '620', 'name': u'Portugal'},
    'PR': {'iso3': 'PRI', 'number': '630', 'name': u'Puerto Rico'},
    'QA': {'iso3': 'QAT', 'number': '634', 'name': u'Catar'},
    'GB': {'iso3': 'GBR', 'number': '826', 'name': u'Reino Unido'},
    'RE': {'iso3': 'REU', 'number': '638', 'name': u'Reunión'},
    'RW': {'iso3': 'RWA', 'number': '646', 'name': u'Ruanda'},
    'RO': {'iso3': 'ROU', 'number': '642', 'name': u'Rumania'},
    'RU': {'iso3': 'RUS', 'number': '643', 'name': u'Rusia'},
    'EH': {'iso3': 'ESH', 'number': '732', 'name': u'República Árabe Saharaui Democrática'},
    'SB': {'iso3': 'SLB', 'number': '090', 'name': u'Islas Salomón'},
    'WS': {'iso3': 'WSM', 'number': '882', 'name': u'Samoa'},
    'AS': {'iso3': 'ASM', 'number': '016', 'name': u'Samoa Americana'},
    'BL': {'iso3': 'BLM', 'number': '652', 'name': u'San Bartolomé'},
    'KN': {'iso3': 'KNA', 'number': '659', 'name': u'San Cristóbal y Nieves'},
    'SM': {'iso3': 'SMR', 'number': '674', 'name': u'San Marino'},
    'MF': {'iso3': 'MAF', 'number': '663', 'name': u'San Martín'},
    'PM': {'iso3': 'SPM', 'number': '666', 'name': u'San Pedro y Miquelón'},
    'VC': {'iso3': 'VCT', 'number': '670', 'name': u'San Vicente y las Granadinas'},
    'SH': {'iso3': 'SHN', 'number': '654', 'name': u'Santa Helena, A. y T.'},
    'LC': {'iso3': 'LCA', 'number': '662', 'name': u'Santa Lucía'},
    'ST': {'iso3': 'STP', 'number': '678', 'name': u'Santo Tomé y Príncipe'},
    'SN': {'iso3': 'SEN', 'number': '686', 'name': u'Senegal'},
    'RS': {'iso3': 'SRB', 'number': '688', 'name': u'Serbia'},
    'SC': {'iso3': 'SYC', 'number': '690', 'name': u'Seychelles'},
    'SL': {'iso3': 'SLE', 'number': '694', 'name': u'Sierra Leona'},
    'SG': {'iso3': 'SGP', 'number': '702', 'name': u'Singapur'},
    'SY': {'iso3': 'SYR', 'number': '760', 'name': u'Siria'},
    'SO': {'iso3': 'SOM', 'number': '706', 'name': u'Somalia'},
    'LK': {'iso3': 'LKA', 'number': '144', 'name': u'Sri Lanka'},
    'SZ': {'iso3': 'SWZ', 'number': '748', 'name': u'Suazilandia'},
    'ZA': {'iso3': 'ZAF', 'number': '710', 'name': u'Sudáfrica'},
    'SD': {'iso3': 'SDN', 'number': '729', 'name': u'Sudán'},
    'SS': {'iso3': 'SSD', 'number': '728', 'name': u'Sudán del Sur'},
    'SE': {'iso3': 'SWE', 'number': '752', 'name': u'Suecia'},
    'CH': {'iso3': 'CHE', 'number': '756', 'name': u'Suiza'},
    'SR': {'iso3': 'SUR', 'number': '740', 'name': u'Surinam'},
    'SJ': {'iso3': 'SJM', 'number': '744', 'name': u'Svalbard y Jan Mayen'},
    'TH': {'iso3': 'THA', 'number': '764', 'name': u'Tailandia'},
    'TW': {'iso3': 'TWN', 'number': '158', 'name': u'Taiwán'},
    'TZ': {'iso3': 'TZA', 'number': '834', 'name': u'Tanzania'},
    'TJ': {'iso3': 'TJK', 'number': '762', 'name': u'Tayikistán'},
    'IO': {'iso3': 'IOT', 'number': '086', 'name': u'Territorio Británico del Océano Índico'},
    'TF': {'iso3': 'ATF', 'number': '260', 'name': u'Territorios Australes Franceses'},
    'TL': {'iso3': 'TLS', 'number': '626', 'name': u'Timor Oriental'},
    'TG': {'iso3': 'TGO', 'number': '768', 'name': u'Togo'},
    'TK': {'iso3': 'TKL', 'number': '772', 'name': u'Tokelau'},
    'TO': {'iso3': 'TON', 'number': '776', 'name': u'Tonga'},
    'TT': {'iso3': 'TTO', 'number': '780', 'name': u'Trinidad y Tobago'},
    'TN': {'iso3': 'TUN', 'number': '788', 'name': u'Túnez'},
    'TC': {'iso3': 'TCA', 'number': '796', 'name': u'Islas Turcas y Caicos'},
    'TM': {'iso3': 'TKM', 'number': '795', 'name': u'Turkmenistán'},
    'TR': {'iso3': 'TUR', 'number': '792', 'name': u'Turquía'},
    'TV': {'iso3': 'TUV', 'number': '798', 'name': u'Tuvalu'},
    'UA': {'iso3': 'UKR', 'number': '804', 'name': u'Ucrania'},
    'UG': {'iso3': 'UGA', 'number': '800', 'name': u'Uganda'},
    'UY': {'iso3': 'URY', 'number': '858', 'name': u'Uruguay'},
    'UZ': {'iso3': 'UZB', 'number': '860', 'name': u'Uzbekistán'},
    'VU': {'iso3': 'VUT', 'number': '548', 'name': u'Vanuatu'},
    'VA': {'iso3': 'VAT', 'number': '336', 'name': u'Ciudad del Vaticano'},
    'VE': {'iso3': 'VEN', 'number': '862', 'name': u'Venezuela'},
    'VN': {'iso3': 'VNM', 'number': '704', 'name': u'Vietnam'},
    'VG': {'iso3': 'VGB', 'number': '092', 'name': u'Islas Vírgenes Británicas'},
    'VI': {'iso3': 'VIR', 'number': '850', 'name': u'Islas Vírgenes de los Estados Unidos'},
    'YE': {'iso3': 'YEM', 'number': '887', 'name': u'Yemen'},
    'DJ': {'iso3': 'DJI', 'number': '262', 'name': u'Yibuti'},
    'ZM': {'iso3': 'ZMB', 'number': '894', 'name': u'Zambia'},
    'ZW': {'iso3': 'ZWE', 'number': '716', 'name': u'Zimbabue'},
}

for k,v in countries.items():
    country_list.append(
        Country(code=k, iso3=v['iso3'], number=v['number'], name=v['name']))