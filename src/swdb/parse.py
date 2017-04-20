import codes
import pandas as pd

from swdb import SWDBResults
from util import COUNTIES


elections = [('P14', '2014/20140603__ca__primary__%s__precinct.csv',
              {'Kamala Harris': 'Kamala D. Harris',
               'James Theis': 'James E. Theis',
               'Betty Yee': 'Betty T. Yee',
               'John Perez': 'John A. Pérez',
               'Tammy Blair': 'Tammy D. Blair',
               'Alma Winston': 'Alma Marie Winston',
               'Bogdan Ambrozewicz': '"Bo" Bogdan Ambrozewicz',
               'Cindy Sheehan': 'Cindy L. Sheehan',
               'Dale Mensing': 'Dale K. Mensing',
               'Diana Conti': 'Diana M. Conti',
               'Edmund G. Brown': 'Edmund G. "Jerry" Brown',
               'Ellen Brown': 'Ellen H. Brown',
               'Harry Lehmann': 'Harry V. Lehmann',
               'Janel Buycks': 'Janel Hyeshia Buycks',
               'Jeffrey Drobman': 'Jeffrey H. Drobman',
               'Jena Goodman': 'Jena F. Goodman',
               'Lawrence Wiesner': 'Lawrence R. Wiesner',
               'Luis Rodriguez': 'Luis J. Rodriguez',
               'Lydia Gutierrez': 'Lydia A. Gutiérrez',
               'Rakesh Christian': 'Rakesh Kumar Christian',
               'Veronica Jacobi': 'Veronica "Roni" Jacobi',
               'Richard Aguirre': 'Richard William Aguirre',
               'Adam Miller': 'Adam J. Miller',
               'Adam Schiff': 'Adam B. Schiff',
               'Adam Plimpton': 'Adam M. Plimpton',
               'Adrienne Edwards': 'Adrienne Nicole Edwards',
               'Alfonso Sanchez': 'Alfonso "Al" Sanchez',
               'Arturo Alas': 'Arturo Enrique Alas',
               'Barbara Mulvaney': 'Barbara L. Mulvaney',
               'Barbi Appelquist': 'Barbi S. Appelquist',
               'Bradly Torgan': 'Bradly S. Torgan',
               'Brent Roske': 'Brent C. Roske',
               'Carlos Arvizu': 'Carlos R. Arvizu',
               'Connie Leyva': 'Connie M. Leyva',
               'David Bruce': 'David Koster Bruce',
               'Dorothy Pineda': 'Dorothy F. Pineda',
               'Douglas Kmiec': 'Douglas William Kmiec',
               'Emidio Soltysik': 'Emidio "Mimi" Soltysik',
               'Esthela Siegrist': 'Esthela Torres Siegrist',
               'Evan Thomas': 'Evan "Ivan" Thomas',
               'Grace Napolitano': 'Grace F. Napolitano',
               'Gregg Fritchle': 'Gregg D. Fritchle',
               'Holly Mitchell': 'Holly J. Mitchell',
               'Ian Calderon': 'Ian C. Calderon',
               'Jerome Horton': 'Jerome E. Horton',
               'Joe Gardner': 'Joe M. Gardner',
               'John Goya': 'John C. Goya',
               'John Lindblad': 'John P. "Jack" Lindblad',
               'Jorge Fuentes': 'Jorge Salomon Fuentes',
               'Kermit Franklin': 'Kermit F. Franklin',
               'Kevin Suscavage': 'Kevin J. Suscavage',
               'Linda Sanchez': 'Linda T. Sanchez',
               'Mario Guerra': 'Mario A. Guerra',
               'Mark Reed': 'Mark S. Reed',
               'Mathew Herd': 'Mark Matthew Herd',
               'Michael Aldapa': 'Michael "Mike" Aldapa',
               'Michael Powelson': 'Michael W. Powelson',
               'Michael Sachs': 'Michael Ian Sachs',
               'Michelle Walker': 'Michelle "Hope" Walker',
               'Norma Torres': 'Norma J. Torres',
               'Patric Verrone': 'Patric M. Verrone',
               'Peter Anderson': 'Peter O. Anderson',
               'Prophet Walker': "Prophet La'Omar Walker",
               'Rafael Dagnesses': 'Rafael Alberto Dagnesses',
               'Ricardo Benitez': 'Ricardo Antonio Benitez',
               'Sally Havice': 'Sally Morales Havice',
               'Sebastian Thomas': 'Sebastian Mark Ridley Thomas',
               'Simona Farrise': 'Simona A. Farrise',
               'Suzette Martinez': 'Suzette M. Martinez',
               'Ted Grose': 'Ted J. Grose',
               'Venice Gamble': 'Venice J. Gamble',
               'William Leader': "William O' Callaghan Leader",
               'William Morrison': 'William "Rodriguez" Morrison',
               'Zein Obagi, Jr.': 'Zein E. Obagi, Jr.',
               'Davdi Valadao': 'David Valadao',
               'Devin Nunes': 'Devin G. Nunes',
               'Henry Perea': 'Henry T. Perea',
               'Jeffrey Gerlach': 'Jeffrey D. Gerlach',
               'John Catano': 'John P. Catano',
               'John Hernandez': 'John S. Hernandez',
               'Shawn Bagley': 'Shawn K. Bagley',
               'Suzanna Marrero': 'Suzanna "Sam" Aguilera Marrero',
               'Pedro Rios': 'Pedro A. Rios',
               'Arthur Moore': 'Arthur "Art" Moore',
               'Beth Gaines': 'Beth B. Gaines',
               'Brigham Smith': 'Brigham Sawyer Smith',
               'Cheryl Brown': 'Cheryl R. Brown',
               'Diane Harkey': 'Diane L. Harkey',
               'Eloise Reyes': 'Eloise Gomez Reyes',
               'Jerry Laws': 'Jerry J. Laws',
               'John Kelly': 'John F. Kelly',
               'Odessia Lee': 'Odessia D. Lee',
               'Robert Buhrle': 'Robert J. (Bob) Buhrle',
               'Cecilia Iglesias': 'Cecilia "Ceci" Iglesias',
               'Donald Wagner': 'Donald P. (Don) Wagner',
               'Drew Leavens': 'Drew E. Leavens',
               'John Cullum': 'John J. Cullum',
               'Karina Onofre': 'Karina "Karina" Onofre',
               'Keith Curry': 'Keith D. Curry',
               'Patricia Bates': 'Patricia C. "Pat" Bates',
               'Paul Glaab': 'Paul G. Glaab',
               'Robert Banuelos': 'Robert John Banuelos',
               'Suzanne Savary': 'Suzanne Joyce Savary',
               'Wendy Leece': 'Wendy Brooks Leece',
               'William Brough': 'William (Bill) Brough',
               'Douglas Van Raam': 'Douglas S. Van Raam',
               'Brian Jones': 'Brian W. Jones',
               'Glenn Miller': 'Glenn A. Miller',
               'James Kimber': 'James H. Kimber',
               'Keri Condley': 'Kerri Condley',
               'William Carns': 'William "Bill" Carns',
               'Yvonne Girard': 'Yvonne Terrell Girard',
               'Anna Eshoo': 'Anna G. Eshoo',
               'Oscar Braun': 'Oscar Alejandro Braun',
               'Richard Fox': 'Richard B. Fox',
               'Ronald Kabat': 'Ronald Paul Kabat',
               'Bernt Wahl': 'Bernt Rainer Wahl',
               'Craig Steckler': 'Craig T. Steckler',
               'Ellen Corbett': 'Ellen M. Corbett',
               'Eugene Ruyle': 'Eugene E. Ruyle',
               'Lawrence Allen': 'Lawrence N. Allen',
               'Richard Gordon': 'Richard S. Gordon',
               'Justin Fareed': 'Justin Donald Fareed',
               'Paul Coyne, Jr.': 'Paul H. Coyne, Jr.',
               'Johnathan Zachariou': 'Jonathan Zachariou',
               'A.J. Thorsson': 'A.J. "Desmond" Thorsson',
               'David Salaverry': 'David Carlos Salaverry',
               'Antonio Amador': 'Antonio C. "Tony" Amador',
               'Karen Davis': 'Karen "Mathews" Davis',
               'Steve Colangelo': 'Steve Anthony Colangelo',
               'Susan Bonilla': 'Susan A. Bonilla',
               'Fotios Tsimboukakis': 'Fotios "Frank" Tsimboukakis',
               'Fred Simon Jr.': 'Fred J. Simon Jr.',
               'John Campbell': 'John W. Campbell',
               'John Edwards': 'John R. Edwards',
               'Kevin Melton': 'Kevin D. Melton',
               'Krik Jorgensen': 'Kirk Jorgensen',
               'Larry Wilske': 'Larry A. Wilske',
               'Rocky Chavez': 'Rocky J. Chávez',
               'Ruben Hernandez': 'Ruben "RJ" Hernandez',
               'Shirley Weber': 'Shirley N. Weber',
               'Susan Davis': 'Susan A. Davis',
               'Wayne True': 'Wayne S. True',
               'Derek Thomas': 'Derek A. Thomas',
               'Teresita Andres': 'Teresita "Tess" Andres',
               'Virginia Goodman': 'Virginia "Mari" Goodman',
               'Catherine Stebbins': 'Catherine Jennet Stebbins',
               'Darrell Fong': 'Darrell R. Fong',
               'Manuel Martin': 'Manuel J. Martin',
               'Michael Barkley': 'Michael J. "Mike" Barkley',
               'Susan Eggman': 'Susan Talamantes Eggman',
               'Jonathan Madison': 'Jonathan Emmanuel Madison',
               'Douglas Tuma': 'Douglas Arthur Tuma',
               'Janice Bonser': 'Janice Marlae Bonser',
               'Phill Tufi': 'Phill A. Tufi'}),
             ('G14', '2014/20141104__ca__general__%s__precinct.csv',
              {'Arthur Moore': 'Arthur "Art" Moore',
               'Charles Bennett, Jr.': 'Charles Bennett Jr.',
               'Antonio C. Amador': 'Antonio C. "Tony" Amador',
               'Joseph McCray, Sr.': 'Joseph McCray Sr.',
               'Suzanna Aguilera-Marrero': 'Suzanna "Sam" Aguilera-Marrero',
               'Fotios Tsimboukakis': 'Fotios "Frank" Tsimboukakis',
               'Patricia C. Bates': 'Patricia C. "Pat" Bates',
               'Ruben Hernandez': 'Ruben "RJ" Hernandez',
               'Virginia Goodman': 'Virginia "Mari" Goodman',
               'Donald P. Wagner': 'Donald P. (Don) Wagner',
               'William Brough': 'William (Bill) Brough',
               'Edmund G. Brown': 'Edmund G. "Jerry" Brown',
               'Rocky J. Chavez': 'Rocky J. Chávez'}),
             ('P16', '2016/20160607__ca__primary__%s__precinct.csv',
              {'Eleanor Garcia': 'Eleanor García',
               'Kenneth Canada': 'Kenneth "Mike" Canada',
               'Juan Mercado-Flores': 'Juan "Charly" Mercado-Flores',
               'Reagan Allvord': 'Terry Reagan Allvord',
               'Juan M. Hidalgo, Jr.': 'Juan M. Hidalgo Jr.',
               'Nicholas Walpert': 'Nicholas "Nick" Walpert',
               'Melinda K. Vasquez': 'Melinda K. Vásquez',
               'Andrew Masiel, Sr.': 'Andrew Masiel Sr.',
               'Teresita Andres': 'Teresita "Tess" Andres',
               'N. Eugene Cleek': 'N Eugene Cleek',
               'Robert Evans': 'Robert (Bob) Evans',
               'Mario Galvan': 'Mario Galván',
               'Greg Coppes': 'Greg "Coach" Coppes',
               'Carlos Taylor': 'Carlos "Chuck" Taylor',
               'Veronica Jacobi': 'Veronica "Roni" Jacobi',
               'William Ostrander': 'William "Bill" Ostrander',
               'Donald Fareed': 'Justin Donald Fareed',
               'Ron Mikulaco': 'Ron "Mik" Mikulaco',
               'Bogdan Ambrozewicz': '"Bo" Bogdan I. Ambrozewicz',
               'S. Monique Limon': 'S. Monique Limón',
               'A. Rab': 'A. (Raji) Rab',
               'Stephan Wolkowicz': 'Stephan "Steven" Wolkowicz',
               'Rudolfo Gaona': 'Rodolfo Rudy Gaona',
               'Linda T. Sanchez': 'Linda T. Sánchez',
               'Michael Adams': 'Scott Michael Adams',
               'John M. W. Moorlach': 'John M.W. Moorlach',
               'William Brough': 'William (Bill) Brough',
               'Michael J. Barkley': 'Michael J. "Mike" Barkley',
               'Jacob Souza': 'Jacob "Jake" Souza',
               'Antonio C. Amador': 'Antonio C. "Tony" Amador',
               'Pierluigi C. Olivero': 'Pierluigi C. Oliverio',
               'Jacob Cabrera': 'Jay Blas Jacob Cabrera',
               'Phlunte Riddle': "Phlunte' Riddle",
               'Sandre R. Swanson': 'Sandré R. Swanson',
               'Nanette Diaz Barragan': 'Nanette Diaz Barragán',
               'Joseph Shammas': 'Joseph "Joe" Shammas',
               'Benny Bernal': 'Benny "Benito" Bernal',
               'Roger Hernandez': 'Roger Hernández',
               })
             ]

for code, pattern, norm in elections:
    for county in COUNTIES:
        print(county)
        try:
            results = SWDBResults(code, county, norm)
        except Exception as e:
            print(e)
            continue

        results.df.to_csv(
            pattern % (county.lower().replace(' ', '_')), index=False)
