age = 24
print("my age is " + str(age) + " years")
print("my age is {0} years".format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))

print("Jan {0}, Feb {1}, Mar {0}, April {2}, May {0}, June {2}, July {0}, August {0}, September {2}, October {0}, "
      "November {2}, December {0}".
      format(31, 28, 30))

print("""Jan {0} 
Feb {1} 
Mar {0}
April {2} 
May {0} 
June {2} 
July {0}
August {0}
September {2} 
October {0} 
November {2} 
December {0}""".
      format(31, 28, 30))
