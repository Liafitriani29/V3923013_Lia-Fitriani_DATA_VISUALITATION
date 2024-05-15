#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

# initializing the data

x = [10, 20, 30, 40]

y = [20, 25, 35, 55]

# plotting the data 
plt.plot(x, y)

plt.show()


# In[4]:


import matplotlib.pyplot as plt

# initializing the data 
x = [10, 20, 30, 40] 
y = [20, 25, 35, 55]

# plotting the data 
plt.plot(x, y)

#Adding title to the plot 
plt.title("Linear graph", fontsize=25, color="green")

plt.show()


# In[5]:


import matplotlib.pyplot as plt

# Initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# Plotting the data
plt.plot(x, y)

# Adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")  # Perbaiki tanda "=" bukan "-"

# Adding Label on the y-axis
plt.ylabel('Y-Axis')  # Perbaiki tanda kutip dan tambahkan tanda petik tutup

# Adding Label on the x-axis
plt.xlabel('X-Axis')

plt.show()


# In[6]:


import matplotlib.pyplot as plt

# Initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# Plotting the data
plt.plot(x, y)

# Adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")

# Adding Label on the y-axis
plt.ylabel('Y-Axis')

# Adding Label on the x-axis with custom labels
plt.xlabel('X-Axis')
plt.xticks(x, labels=["one", "two", "three", "four"]) 

# Setting the limit of y-axis
plt.ylim(0, 80)

# Adding Legends
plt.legend(["GFG"])

plt.show()


# In[7]:


import matplotlib.pyplot as plt

# Initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]


fig = plt.figure(figsize=(5, 4))

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])


ax2 = fig.add_axes([1, 0.1, 0.8, 0.8])  


ax1.plot(x, y)
ax2.plot(y, x)


plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)
plt.title("Linear graph", fontsize=25, color="green")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.ylim(0, 80)
plt.xticks(x, labels=["one", "two", "three", "four"])
plt.legend(["GFG"])

plt.show()


# In[9]:


import pandas as pd

# Membaca file CSV
data = pd.read_csv("tips.csv")

# Menampilkan 10 baris pertama dari data
print(data.head(10))


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

plt.scatter(data['day'], data['tip'])

plt.title("Scatter Plot")

plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

plt.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])

plt.title("Scatter Plot")

plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")
plt.plot(data['tip'])
plt.plot(data['size'])
plt.title("Line Plot")
plt.xlabel('Index') 
plt.ylabel('Value')

plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")


plt.bar(data['day'], data['tip'])

plt.title("Bar Chart")

plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv("tips.csv")

# Membuat histogram dari kolom 'total_bill'
plt.hist(data['total_bill'])

# Menambahkan judul plot
plt.title("Histogram")

# Menampilkan plot
plt.show()


# In[15]:


import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('tips.csv')

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars)

plt.title("Car Data")

plt.show()


# In[17]:


import matplotlib.pyplot as plt

year = ['2010', '2012', '2014', '2016', '2018']
production = [25, 15, 35, 30, 10]


plt.bar(year, production)

plt.savefig("output.jpg")


plt.savefig("output1.jpg", facecolor='yellow', bbox_inches="tight", 
            pad_inches=0.3, transparent=True)

plt.show()


# In[ ]:




