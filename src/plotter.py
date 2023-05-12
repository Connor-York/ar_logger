import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file into a pandas dataframe
df = pd.read_csv('/content/Fast_Patrol_1.csv')

df2 = pd.read_csv('/content/Slow_Patrol_1.csv') #Assuming slower is longer 

#print(df.index.stop)
#print(df2.index.stop)

diff = df2.index.stop - df.index.stop

timediff = df2["Timestamp"].iloc[df2.index.stop-1]


filler = df.iloc[[df.index.stop-1],:]


#df.iat[df.index.stop-1,1] = timediff

#for i in range(diff):
#  df = pd.concat([df,filler])

print(df)
print(df2)

# Create plot using matplotlib
plt.step(df["Timestamp"], df.index, where='post')
plt.step(df2["Timestamp"],df2.index, where='post')

# Add labels and title
plt.xlabel('Time (s)')
#plt.xticks(np.arange(0,max(df2["Timestamp"]),5))
plt.ylabel('Row Number')
plt.title('Time vs Row Number')
plt.legend(['Fast', 'Slow'])
#plt.grid()

# Show plot
plt.show()
