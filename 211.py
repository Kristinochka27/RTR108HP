#import random
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black", "#800080", "#FFFF00", "#800000" ]
#number=random.randint(1,11)
#number.range(11)
print "<html>"
for k in range(11):
	print ("<font color=\"%s\">"%colour[k]), k, k*k,"</font>", "<br>"
print "</html>"
