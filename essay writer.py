#essay writer
essay_title = input("Title for your essay: ")
your_name = input("Input your name: ")
essay = input("Write the essay here: ")
print (essay_title+"\n\n"+essay+"\n\n"+"Made by "+your_name)

s = input("Export as html? (y/n)")

if(s=="y"):
  f = open("essay.html", "w")
  f.write('<!DOCTYPE html> <html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> </head> <body>')
  f.write("<p style='text-align:right'>"+your_name+"</p>")
  f.write("<br><h1 style='text-align:center'>"+essay_title+"</h1>")
  f.write("<br><p>"+essay+"</p")

if(s=="n"):
  print("Why?")
