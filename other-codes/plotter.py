from myUtils import load_one_result_set

def Regret(SAVE_PATH):
    df_concat = load_one_result_set(SAVE_PATH)
#    names = df.bsuite_id.unique()
#    df1 = df.loc[df['bsuite_id'] == names[0], 'total_bad_episodes']

    by_row_index = df_concat.groupby(df_concat.index)
    df_means = by_row_index.mean()
    return     df_means.steps.values , df_means.total_bad_episodes.values


steps,vals = Regret('results/deepsea/L20-LONG')
steps1 , vals_bdqn = Regret('results/deepsea/BDQNL20-LONG')
steps2 , vals_ts = Regret('results/deepsea/TS20-LONG')

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(steps, vals, color='#CC4F1B',label='Sparser_PI')#,linestyle=linesty, marker='d',markerfacecolor='None',markersize=mks,markevery=mkstep)
ax.plot(steps1, vals_bdqn, color='#1B2ACC',label='BDQN')#,linestyle=linesty, marker='>',markerfacecolor='None',markersize=mks,markevery=mkstep)
ax.plot(steps2, vals_ts, color='#3F7F4C',label='PSRL')

legend = ax.legend(loc='lower right', shadow=False)
plt.xlabel('Time (t)')
plt.ylabel('Regret')
plt.title('L=20')
plt.grid(False)
plt.savefig("L20.png")
plt.show()
