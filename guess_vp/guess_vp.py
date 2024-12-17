import random

vp_terms = [
    ("John Adams", 1789, 1797),
    ("Thomas Jefferson", 1797, 1801),
    ("Aaron Burr", 1801, 1805),
    ("George Clinton", 1805, 1812),
    ("Elbridge Gerry", 1813, 1814),
    ("Daniel D. Tompkins", 1817, 1825),
    ("John C. Calhoun", 1825, 1832),
    ("Martin Van Buren", 1833, 1837),
    ("Richard M. Johnson", 1837, 1841),
    ("John Tyler", 1841, 1841),
    ("George M. Dallas", 1845, 1849),
    ("Millard Fillmore", 1849, 1850),
    ("William R. King", 1853, 1853),
    ("John C. Breckinridge", 1857, 1861),
    ("Hannibal Hamlin", 1861, 1865),
    ("Andrew Johnson", 1865, 1865),
    ("Schuyler Colfax", 1869, 1873),
    ("Henry Wilson", 1873, 1875),
    ("William A. Wheeler", 1877, 1881),
    ("Chester A. Arthur", 1881, 1881),
    ("Thomas A. Hendricks", 1885, 1885),
    ("Levi P. Morton", 1889, 1893),
    ("Adlai E. Stevenson", 1893, 1897),
    ("Garret A. Hobart", 1897, 1899),
    ("Theodore Roosevelt", 1901, 1901),
    ("Charles W. Fairbanks", 1905, 1909),
    ("James S. Sherman", 1909, 1912),
    ("Thomas R. Marshall", 1913, 1921),
    ("Calvin Coolidge", 1921, 1923),
    ("Charles G. Dawes", 1925, 1929),
    ("Charles Curtis", 1929, 1933),
    ("John N. Garner", 1933, 1941),
    ("Henry A. Wallace", 1941, 1945),
    ("Harry S. Truman", 1945, 1945),
    ("Alben W. Barkley", 1949, 1953),
    ("Richard Nixon", 1953, 1961),
    ("Lyndon B. Johnson", 1961, 1963),
    ("Hubert Humphrey", 1965, 1969),
    ("Spiro Agnew", 1969, 1973),
    ("Gerald Ford", 1973, 1974),
    ("Nelson Rockefeller", 1974, 1977),
    ("Walter Mondale", 1977, 1981),
    ("George H. W. Bush", 1981, 1989),
    ("Dan Quayle", 1989, 1993),
    ("Al Gore", 1993, 2001),
    ("Dick Cheney", 2001, 2009),
    ("Joe Biden", 2009, 2017),
    ("Mike Pence", 2017, 2021),
    ("Kamala Harris", 2021, 2024),
]

name, term_start, term_end = random.choice(vp_terms)

print(f"{name} is currently Vice President.")
year = int(input("What year might it be?"))
start = int(term_start)
end = int(term_end)

if year >= start and year <= end:
    print("It could be!")
else: print("Sorry time traveler. That\'s not right.")
print(f"{name} was VP from {start} to {end}.")


# TODO print "[NAME] is currently Vice President."
# TODO prompt the user, "What year might it be?"
# TODO if correct, print "It could be!"
# TODO if incorrect, print "Sorry time traveler. That's not right."
# TODO print "[NAME] was VP from [START] to [END]."
