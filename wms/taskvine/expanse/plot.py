import matplotlib.pyplot as plt
import scipy

cores = 12
apps = {'1W-20C':
                    {2000:[30.23896598815918, 33.01067900657654, 31.93217706680298], 
                     1000:[32.830016136169434, 33.32467603683472, 32.17509603500366], 
                     500:[31.47571587562561, 31.87609601020813, 32.569047927856445], 
                     100:[36.298343896865845, 32.221266984939575,  31.79244303703308]}, 

        '2W-10C':
                    {2000:[32.20032596588135, 33.125560998916626, 33.75481915473938],
                     1000:[34.44443893432617, 40.707700967788696, 35.25127387046814],
                     500:[34.66109299659729, 33.137322187423706, 34.66109299659729],
                     100:[30.037398099899292, 31.953300952911377, 29.88383984565735]},

        '4W-5C':
                    {2000:[39.79434418678284, 39.230324029922485, 39.009588956832886],
                     1000:[42.35685706138611, 40.35938000679016, 39.94182896614075],
                     500:[38.68467402458191, 39.34564399719238, 39.67868494987488],
                     100:[29.0972261428833, 31.20712900161743, 35.75804686546326]},
        '10W-2C':
                    {2000:[47.52444005012512, 48.70596408843994, 48.52556586265564],
                     1000:[45.655417919158936, 45.74582505226135, 45.265625],
                     500:[41.49470806121826, 42.39931797981262, 42.52536201477051],
                     100:[29.974113941192627, 35.10733509063721, 30.370847940444946]},   
                    }

                 

fig, axs = plt.subplots(1, 1, squeeze=False)


ax = axs[0][0]

info = {'x':[], 'y':[], 'yerr':[]}
key = '1W-20C'
for job_count in apps[key]:
    info['x'].append(job_count)
    info['y'].append(sum(apps[key][job_count])/len(apps[key][job_count]))
    info['yerr'].append(scipy.stats.sem(apps[key][job_count]))
ax.errorbar(info['x'], info['y'], info['yerr'], capsize=5,  linestyle='-', label=key)


info = {'x':[], 'y':[], 'yerr':[]}
key = '2W-10C'
for job_count in apps[key]:
    info['x'].append(job_count)
    info['y'].append(sum(apps[key][job_count])/len(apps[key][job_count]))
    info['yerr'].append(scipy.stats.sem(apps[key][job_count]))
ax.errorbar(info['x'], info['y'], info['yerr'], capsize=5,  linestyle='-', label=key)

info = {'x':[], 'y':[], 'yerr':[]}
key = '4W-5C'
for job_count in apps[key]:
    info['x'].append(job_count)
    info['y'].append(sum(apps[key][job_count])/len(apps[key][job_count]))
    info['yerr'].append(scipy.stats.sem(apps[key][job_count]))
ax.errorbar(info['x'], info['y'], info['yerr'], capsize=5,  linestyle='-', label=key)

info = {'x':[], 'y':[], 'yerr':[]}
key = '10W-2C'
for job_count in apps[key]:
    info['x'].append(job_count)
    info['y'].append(sum(apps[key][job_count])/len(apps[key][job_count]))
    info['yerr'].append(scipy.stats.sem(apps[key][job_count]))
ax.errorbar(info['x'], info['y'], info['yerr'], capsize=5,  linestyle='-', label=key)

ax.set_xlabel('Ephemeral File Count',fontsize=12)
ax.set_ylabel('Read Block Time (s)', fontsize=12)
ax.set_yscale('log')
#ax.set_xlim(left=500)
ax.set_ylim(bottom=28)
plt.title("Time to execute a total 4000 Reads from N distinct 10MB files\n using local disk with 20 cores partitioned")
ax.legend()

width = 6.4 * 1
height = 4.8 * 1
fig.set_size_inches(w=width, h=height)
fig.savefig('graphs/local.png')
plt.show()


