import io
with open('test.txt', 'wb') as f:
    file = io.BufferedWriter(f)
    file.write(b'This is my buffer write  knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical, and computational skills needed to meet the large-scale data science challenges of todays professional world. You will learn all the stack required to work in data science, data analytics, and big data industry including cloud infrastructure and real-time industry projects')
    file.write(b'This is my second line that I am trying to write')
    file.flush()

with open('test.txt', 'rb') as f:
    file = io.BufferedReader(f)
    data = file.read(100)
    print(data)