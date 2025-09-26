import matplotlib.pyplot as ptl

profit = [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def chart():
    ptl.plot(profit, month)
    ptl.title("Profit Chart (per month)")
    ptl.xlabel("Profit")
    ptl.ylabel("Month")
    ptl.show()
chart()

def bar():
    ptl.bar(profit, month)
    ptl.title("Bar Chart")
    ptl.xlabel("Profit")
    ptl.ylabel("Month")
bar()