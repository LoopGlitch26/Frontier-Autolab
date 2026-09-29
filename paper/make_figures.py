"""Regenerate the paper's data figures from ../results/all_runs_scores.csv."""
import csv, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
T=['frontier_accuracy','timing','layer_choice','reinvention_courage','hindsight_leakage']
F=['playbook_consistency','plausibility','non_consensus','layer_choice','grounded']
runs={}
for d in csv.DictReader(open('../results/all_runs_scores.csv')):
    names=T if d['mode']=='training' else F
    runs.setdefault(d['run'],[]).append((d['era'],int(d['year']),d['mode'],d['company'],int(d['reported_total']),[int(d[n]) for n in names]))
cols={'run-001':'#1f4e79','run-002':'#c55a11','run-003':'#548235','run-004':'#7030a0'}
mk={'run-001':'o','run-002':'s','run-003':'^','run-004':'D'}
lab={r:'Run '+r[-3:] for r in runs}
x=np.arange(9); years=[e[1] for e in runs['run-001']]
fig,ax=plt.subplots(figsize=(6.3,2.7)); ax.axvspan(5.5,8.5,color='#eeeeee',zorder=0)
ax.text(2.5,73.2,'training eras (scored against history)',ha='center',fontsize=8,color='#444'); ax.text(7,73.2,'live + forecast',ha='center',fontsize=8,color='#444')
for r,e in runs.items(): ax.plot(x,[v[4] for v in e],marker=mk[r],color=cols[r],lw=1.4,ms=4,label=lab[r])
ax.set_xticks(x); ax.set_xticklabels([f'E{i+1}\n{y}' for i,y in enumerate(years)]); ax.set_ylim(48,75); ax.set_ylabel('Published era total (0–100)')
ax.legend(ncol=4,frameon=False,loc='lower center',bbox_to_anchor=(0.5,-0.42)); ax.grid(axis='y',color='#dddddd',lw=0.6)
fig.tight_layout(); fig.savefig('figures/fig_trajectories.pdf',bbox_inches='tight')
fig,axs=plt.subplots(1,4,figsize=(6.5,1.9),sharey=True)
for a,(r,e) in zip(axs,runs.items()):
    tr=[v for v in e if v[2]=='training']; h=np.array([v[5][4] for v in tr]); t=np.array([v[4] for v in tr]); jit=np.linspace(-0.08,0.08,len(h))
    a.scatter(h+jit,t,color=cols[r],s=16,marker=mk[r],zorder=3)
    for hv,tv,v in zip(h+jit,t,tr): a.annotate(v[0],(hv,tv),fontsize=6,xytext=(3,2),textcoords='offset points',color='#555')
    m,b=np.polyfit(h,t,1); xs=np.linspace(h.min()-.3,h.max()+.3,10); a.plot(xs,m*xs+b,color=cols[r],lw=1,ls='--')
    a.set_title(f'{lab[r]}  (r = {np.corrcoef(h,t)[0,1]:.2f})',fontsize=8); a.set_xlabel('Hindsight subscore\n(10 = no leakage)',fontsize=7); a.set_xlim(3.3,8.7); a.grid(color='#eeeeee',lw=0.5)
axs[0].set_ylabel('Era total'); fig.tight_layout(); fig.savefig('figures/fig_leakage.pdf',bbox_inches='tight')
names=['Frontier\naccuracy','Timing','Layer\nchoice','Reinvention\ncourage','Hindsight\n(10 = none)']
fig,ax=plt.subplots(figsize=(6.3,2.3))
for i,(r,e) in enumerate(runs.items()):
    tr=[v for v in e if v[2]=='training']; ax.bar(np.arange(5)+(i-1.5)*0.2,[np.mean([v[5][k] for v in tr]) for k in range(5)],0.2,color=cols[r],label=lab[r])
ax.set_xticks(range(5)); ax.set_xticklabels(names); ax.set_ylim(0,10); ax.set_ylabel('Mean training subscore')
ax.legend(ncol=4,frameon=False,loc='upper center',bbox_to_anchor=(0.5,1.2)); ax.grid(axis='y',color='#dddddd',lw=0.6)
fig.tight_layout(); fig.savefig('figures/fig_subscores.pdf',bbox_inches='tight')
fig,ax=plt.subplots(figsize=(3.1,2.6))
for r,e in runs.items(): ax.scatter([2*sum(v[5]) for v in e],[v[4] for v in e],color=cols[r],marker=mk[r],s=16,label=lab[r])
ax.plot([50,75],[50,75],color='#999',lw=0.8,ls=':'); ax.set_xlabel('Subscore sum × 2'); ax.set_ylabel('Published total'); ax.set_xlim(50,75); ax.set_ylim(50,75)
ax.legend(frameon=False,fontsize=7); ax.grid(color='#eeeeee',lw=0.5); fig.tight_layout(); fig.savefig('figures/fig_aggregation.pdf',bbox_inches='tight')
