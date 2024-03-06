import matplotlib.pyplot as plt 
fig,ax=plt.subplot()

fruits = ['a','o','b','l']
counts = [10,29,30,20]
bar_labels = ['red','blue','_orange','brown']
bar_colors = ['tab:red','tab:blue','tab:orange','tab:brown']

ax.bar(fruits,counts,label=bar_labels,color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('fruit supply by kind & color')
ax.legend(title='fruit color')

plt.savefig('bars.png',bbox_inches='tight')


cat = ['bored','happy','happy','happy','happy','bored']
dog = ['bored','bored','bored','happy','happy','bored']
activity=['combing','eating','play','sleep','bark','enjoy']


fig,ax=plt.subplot()

ax.plot(activity,dog,label='dog')
ax.plot(activity,cat,label='cat')
ax.legend()

plt.savefig('lines.png',bbox_inches='tight')