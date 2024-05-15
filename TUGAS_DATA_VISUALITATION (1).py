#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# printing the top 10 rows
display(data.head(10))


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.scatter(data['Category'], data['Quantity'])

# Adding Title to the plot
plt.title("Test")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.plot(data['Category'])
plt.plot(data['Quantity'])


# Adding Title to the plot
plt.title("Line Plot")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('line.png', dpi=300, bbox_inches='tight')

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv("Data Sales3.csv", delimiter=";")

# Menghitung jumlah Quantity untuk setiap Category
category_counts = data.groupby('Category')['Quantity'].sum()

# Menggunakan bar plot untuk memvisualisasikan jumlah Quantity tiap Category
plt.figure(figsize=(10, 6))  # Mengatur ukuran gambar plot
plt.bar(category_counts.index, category_counts.values)

# Menambahkan judul dan label sumbu
plt.title("Total Quantity per Category")
plt.xlabel('Category')
plt.ylabel('Total Quantity')

# Memutar label sumbu x jika diperlukan agar lebih mudah dibaca
plt.xticks(rotation=45, ha='right')

# Menyimpan plot sebagai file PNG dengan resolusi tinggi
plt.savefig('bar.png', dpi=300, bbox_inches='tight')

# Menampilkan plot
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.hist(data['Category'])


# Adding Title to the plot
plt.title("Histogram")

# Save the plot as a PNG file
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
sales = ['Category', 'Quantity']
datasales = [23, 10]

plt.pie(datasales, labels=sales)

plt.title("Sales Data")

# Save the plot as a PNG file
plt.savefig('pie.png', dpi=300, bbox_inches='tight')

plt.show()

