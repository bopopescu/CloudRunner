'''tzinfo timezone information for Egypt.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Egypt(DstTzInfo):
    '''Egypt timezone definition. See datetime.tzinfo for details'''

    zone = 'Egypt'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1940,7,14,22,0,0),
d(1940,9,30,21,0,0),
d(1941,4,14,22,0,0),
d(1941,9,15,21,0,0),
d(1942,3,31,22,0,0),
d(1942,10,26,21,0,0),
d(1943,3,31,22,0,0),
d(1943,10,31,21,0,0),
d(1944,3,31,22,0,0),
d(1944,10,31,21,0,0),
d(1945,4,15,22,0,0),
d(1945,10,31,21,0,0),
d(1957,5,9,22,0,0),
d(1957,9,30,21,0,0),
d(1958,4,30,22,0,0),
d(1958,9,30,21,0,0),
d(1959,4,30,23,0,0),
d(1959,9,30,0,0,0),
d(1960,4,30,23,0,0),
d(1960,9,30,0,0,0),
d(1961,4,30,23,0,0),
d(1961,9,30,0,0,0),
d(1962,4,30,23,0,0),
d(1962,9,30,0,0,0),
d(1963,4,30,23,0,0),
d(1963,9,30,0,0,0),
d(1964,4,30,23,0,0),
d(1964,9,30,0,0,0),
d(1965,4,30,23,0,0),
d(1965,9,30,0,0,0),
d(1966,4,30,23,0,0),
d(1966,10,1,0,0,0),
d(1967,4,30,23,0,0),
d(1967,10,1,0,0,0),
d(1968,4,30,23,0,0),
d(1968,10,1,0,0,0),
d(1969,4,30,23,0,0),
d(1969,10,1,0,0,0),
d(1970,4,30,23,0,0),
d(1970,10,1,0,0,0),
d(1971,4,30,23,0,0),
d(1971,10,1,0,0,0),
d(1972,4,30,23,0,0),
d(1972,10,1,0,0,0),
d(1973,4,30,23,0,0),
d(1973,10,1,0,0,0),
d(1974,4,30,23,0,0),
d(1974,10,1,0,0,0),
d(1975,4,30,23,0,0),
d(1975,10,1,0,0,0),
d(1976,4,30,23,0,0),
d(1976,10,1,0,0,0),
d(1977,4,30,23,0,0),
d(1977,10,1,0,0,0),
d(1978,4,30,23,0,0),
d(1978,10,1,0,0,0),
d(1979,4,30,23,0,0),
d(1979,10,1,0,0,0),
d(1980,4,30,23,0,0),
d(1980,10,1,0,0,0),
d(1981,4,30,23,0,0),
d(1981,10,1,0,0,0),
d(1982,7,24,23,0,0),
d(1982,10,1,0,0,0),
d(1983,7,11,23,0,0),
d(1983,10,1,0,0,0),
d(1984,4,30,23,0,0),
d(1984,10,1,0,0,0),
d(1985,4,30,23,0,0),
d(1985,10,1,0,0,0),
d(1986,4,30,23,0,0),
d(1986,10,1,0,0,0),
d(1987,4,30,23,0,0),
d(1987,10,1,0,0,0),
d(1988,4,30,23,0,0),
d(1988,10,1,0,0,0),
d(1989,5,5,23,0,0),
d(1989,10,1,0,0,0),
d(1990,4,30,23,0,0),
d(1990,10,1,0,0,0),
d(1991,4,30,23,0,0),
d(1991,10,1,0,0,0),
d(1992,4,30,23,0,0),
d(1992,10,1,0,0,0),
d(1993,4,30,23,0,0),
d(1993,10,1,0,0,0),
d(1994,4,30,23,0,0),
d(1994,10,1,0,0,0),
d(1995,4,27,22,0,0),
d(1995,9,28,21,0,0),
d(1996,4,25,22,0,0),
d(1996,9,26,21,0,0),
d(1997,4,24,22,0,0),
d(1997,9,25,21,0,0),
d(1998,4,23,22,0,0),
d(1998,9,24,21,0,0),
d(1999,4,29,22,0,0),
d(1999,9,30,21,0,0),
d(2000,4,27,22,0,0),
d(2000,9,28,21,0,0),
d(2001,4,26,22,0,0),
d(2001,9,27,21,0,0),
d(2002,4,25,22,0,0),
d(2002,9,26,21,0,0),
d(2003,4,24,22,0,0),
d(2003,9,25,21,0,0),
d(2004,4,29,22,0,0),
d(2004,9,30,21,0,0),
d(2005,4,28,22,0,0),
d(2005,9,29,21,0,0),
d(2006,4,27,22,0,0),
d(2006,9,21,21,0,0),
d(2007,4,26,22,0,0),
d(2007,9,27,21,0,0),
d(2008,4,24,22,0,0),
d(2008,9,25,21,0,0),
d(2009,4,23,22,0,0),
d(2009,9,24,21,0,0),
d(2010,4,29,22,0,0),
d(2010,9,30,21,0,0),
d(2011,4,28,22,0,0),
d(2011,9,29,21,0,0),
d(2012,4,26,22,0,0),
d(2012,9,27,21,0,0),
d(2013,4,25,22,0,0),
d(2013,9,26,21,0,0),
d(2014,4,24,22,0,0),
d(2014,9,25,21,0,0),
d(2015,4,23,22,0,0),
d(2015,9,24,21,0,0),
d(2016,4,28,22,0,0),
d(2016,9,29,21,0,0),
d(2017,4,27,22,0,0),
d(2017,9,28,21,0,0),
d(2018,4,26,22,0,0),
d(2018,9,27,21,0,0),
d(2019,4,25,22,0,0),
d(2019,9,26,21,0,0),
d(2020,4,23,22,0,0),
d(2020,9,24,21,0,0),
d(2021,4,29,22,0,0),
d(2021,9,30,21,0,0),
d(2022,4,28,22,0,0),
d(2022,9,29,21,0,0),
d(2023,4,27,22,0,0),
d(2023,9,28,21,0,0),
d(2024,4,25,22,0,0),
d(2024,9,26,21,0,0),
d(2025,4,24,22,0,0),
d(2025,9,25,21,0,0),
d(2026,4,23,22,0,0),
d(2026,9,24,21,0,0),
d(2027,4,29,22,0,0),
d(2027,9,30,21,0,0),
d(2028,4,27,22,0,0),
d(2028,9,28,21,0,0),
d(2029,4,26,22,0,0),
d(2029,9,27,21,0,0),
d(2030,4,25,22,0,0),
d(2030,9,26,21,0,0),
d(2031,4,24,22,0,0),
d(2031,9,25,21,0,0),
d(2032,4,29,22,0,0),
d(2032,9,30,21,0,0),
d(2033,4,28,22,0,0),
d(2033,9,29,21,0,0),
d(2034,4,27,22,0,0),
d(2034,9,28,21,0,0),
d(2035,4,26,22,0,0),
d(2035,9,27,21,0,0),
d(2036,4,24,22,0,0),
d(2036,9,25,21,0,0),
d(2037,4,23,22,0,0),
d(2037,9,24,21,0,0),
        ]

    _transition_info = [
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
        ]

Egypt = Egypt()

