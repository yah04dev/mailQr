# mailQr
## The Idea
 when I entred to my university i finded that the administration have a website you enter to the site and input you university id and date of birth and the site gives you your university email and password wich makes me and makes other guys able to steal thier friends emails because the univirsity ids and date of births are in the smate site in the accepted students list
## my solution
i built a python tool with tkinter gui that the administration guy enter the student id and the printer automatically prints qr code containing email and password from sqlite database with the default printer quickly using ***mspaint /pt*** command , that they can use this tool the day of giving the student student card
## observation
because the emails provider are diffrent between univ and other you need to import your data to the Database using ***csv*** and ***sqlite studio*** using tools>import
you can convert all database types to csv and even json with a lot of online and offline tools
the database table named ***mailiste*** and it contains
**** "id"	TEXT,
	"email"	INTEGER,
	"passd"	INTEGER****
  
