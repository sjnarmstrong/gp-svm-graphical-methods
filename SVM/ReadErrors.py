import numpy as np
f = np.load("OutputStats.npz")



problems = [('Versicolor', 'Virginica'),('Versicolor','Setosa'),('Virginica', 'Setosa')]

CostValues=2.0**np.arange(-6,7)
medians, UQ, LQ, mean, errors, Verrors, Allpstrings = [f[dataset] for dataset in f.files]


meanV = np.mean(Verrors, axis=3)
bestV = np.argmax(meanV, axis=2).reshape((3,4,1,1))
I,J,K,L = np.ogrid[:3,:4,:13,:50]
bVParams=Allpstrings[I,J,bestV,L]
bVerrors=Verrors[I,J,bestV,L]



bestV2 = np.argmax(bVerrors, axis=3)
I,J,K = np.ogrid[:3,:4,:1]
bVParams2=bVParams[I,J,K,bestV2].squeeze(axis=2)
bVerrors2=bVerrors[I,J,K,bestV2].squeeze(axis=2)


#bVParams=bVParams.squeeze(axis=2)
#bVerrors=bVerrors.squeeze(axis=2)





bestV = np.argmax(Verrors, axis=3)
I,J,K = np.ogrid[:3,:4,:13]
bVParams=Allpstrings[I,J,K,bestV]
bVerrors=Verrors[I,J,K,bestV]
#bestV2 = np.argmax(bVerrors, axis=2)
#I,J = np.ogrid[:3,:4]
#bVParams2=bVParams[I,J,bestV2]
#bVerrors2=bVerrors[I,J,bestV2]

mins=np.min(errors, axis=3)
maxs=np.max(errors, axis=3)

TotalVerror = np.sum(Verrors, axis = 3)

minCs = np.argmin(TotalVerror[:,:,5:], axis = 2)
maxCs = np.argmax(TotalVerror[:,:,5:], axis = 2)

summaryMeans=[]
summaryMedians=[]
summaryMins=[]
summaryMaxs=[]
summaryUQs=[]
summaryLQs=[]
for i in range(3):
    holdRowMeans=[]
    holdRowMedians=[]
    holdRowUQs=[]
    holdRowLQs=[]
    holdRowMins=[]
    holdRowMaxs=[]
    for j in range(4):
        holdRowMeans.append([mean[i][j][minCs[i,j]],mean[i][j][maxCs[i,j]]])
        holdRowMedians.append([medians[i][j][minCs[i,j]],medians[i][j][maxCs[i,j]]])
        holdRowUQs.append([UQ[i][j][minCs[i,j]],UQ[i][j][maxCs[i,j]]])
        holdRowLQs.append([LQ[i][j][minCs[i,j]],LQ[i][j][maxCs[i,j]]])
        holdRowMins.append([mins[i][j][minCs[i,j]],mins[i][j][maxCs[i,j]]])
        holdRowMaxs.append([maxs[i][j][minCs[i,j]],maxs[i][j][maxCs[i,j]]])
    summaryMeans.append(holdRowMeans)
    summaryMedians.append(holdRowMedians)
    summaryUQs.append(holdRowUQs)
    summaryLQs.append(holdRowLQs)
    summaryMins.append(holdRowMins)
    summaryMaxs.append(holdRowMaxs)

headerTemplate = """   
\\begin{{figure}}[H]
"""
header2="""
\\begin{{subfigure}}[b]{{0.49\\textwidth}}
\\begin{{tikzpicture}}
\\begin{{axis}}
[
ytick={{1, 2, 3, 4}},
yticklabels={{Linear, Polynomial, Radial basis, Sigmoid}},
width=0.8\\textwidth
]
"""
plotTemplate = """
    \\addplot+[
    boxplot prepared={{
    	median={median},
    	upper quartile={uq},
    	lower quartile={lq},
    	upper whisker={maxs},
    	lower whisker={mins}
    }},
    ] coordinates {{}};
"""
footer1="""
\\end{{axis}}
\\end{{tikzpicture}}
\\caption{{{ctext}}}
\\end{{subfigure}}"""
footerTemplate="""
\\caption{{Summary of accuracies achieved for {problemText}}}
\\label{{fig:PB:{problemText2}}}
\\end{{figure}}

"""

outputstring=""
for i,pr in enumerate(problems):
    problemText = pr[0]+" vs "+pr[1]
    problemText2 = problemText.replace(" ","_")
    outputstring += headerTemplate.format()
    outputstring += header2.format()
    for funcnr in range(4):
        params={"median":summaryMedians[i][funcnr][0],
                "uq":summaryUQs[i][funcnr][0],
                "lq":summaryLQs[i][funcnr][0],
                "mins":summaryMins[i][funcnr][0],
                "maxs":summaryMaxs[i][funcnr][0],
                "problemText":problemText,
                "problemText2":problemText2,
                "ctext":"Worst value for $C$"}
        outputstring += plotTemplate.format(**params)
    outputstring+=footer1.format(**params)
    outputstring += header2.format()
    for funcnr in range(4):
        params={"median":summaryMedians[i][funcnr][1],
                "uq":summaryUQs[i][funcnr][1],
                "lq":summaryLQs[i][funcnr][1],
                "mins":summaryMins[i][funcnr][1],
                "maxs":summaryMaxs[i][funcnr][1],
                "problemText":problemText,
                "problemText2":problemText2,
                "ctext":"Best value for $C$"}
        outputstring += plotTemplate.format(**params)
    outputstring+=footer1.format(**params)
    outputstring+=footerTemplate.format(**params)
with open("Output/errorsPlots.tex",'w') as fp :
    fp.write(outputstring)
    
    
CValsToShow=[1,4,6,12]    
    
outputstring=""
for i,pr in enumerate(problems):
    problemText = pr[0]+" vs "+pr[1]
    problemText2 = problemText.replace(" ","_")
    outputstring += headerTemplate.format()
    for CvalI in CValsToShow:
        outputstring += header2.format()
        for funcnr in range(4):
            params={"median":medians[i][funcnr][CvalI],
                    "uq":UQ[i][funcnr][CvalI],
                    "lq":LQ[i][funcnr][CvalI],
                    "mins":mins[i][funcnr][CvalI],
                    "maxs":maxs[i][funcnr][CvalI],
                    "problemText":problemText,
                    "problemText2":problemText2,
                    "ctext":"$C=%.2f$"%bVParams[i][funcnr][CvalI][4]}
            outputstring += plotTemplate.format(**params)
        outputstring+=footer1.format(**params)

    outputstring+=footerTemplate.format(**params)
with open("Output/errorsPlots2.tex",'w') as fp :
    fp.write(outputstring)
    
    
tableFormat = """
\\begin{{table}}[H]
\\centering
\\begin{{tabular}}{{|c|l|l|l|l|l|}}
\\hline
\\multirow{{2}}{{*}}{{\\textbf{{Problem}}}}                                                              & \\multicolumn{{1}}{{c|}}{{\\multirow{{2}}{{*}}{{\\textbf{{Function}}}}}} & \\multicolumn{{4}}{{l|}}{{\\textbf{{Converged Parameters}}}} \\\\ \\cline{{3-6}} 
                                                                                               & \\multicolumn{{1}}{{c|}}{{}}                                   & $d$       & $\\gamma$       & $C_0$      & $C$      \\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Versicolor\\\\ vs \\\\ Virginica\\end{{tabular}}}}}} & Linear                        & -& -& -& {params[0][0][4]:.2f} \\\\ \\cline{{2-6}} 
                                                                                               & Polynomial                                              & {params[0][1][1]:.2f}& {params[0][1][2]:.2f}& {params[0][1][3]:.2f}& {params[0][1][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & \\begin{{tabular}}[c]{{@{{}}l@{{}}}}Radial\\\\ basis\\end{{tabular}}   & -& {params[0][2][2]:.2f}& -& {params[0][2][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & Sigmoid                                                  & -& {params[0][3][2]:.2f}& {params[0][3][3]:.2f}& {params[0][3][4]:.2f}\\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Versicolor\\\\ vs \\\\ Setosa\\end{{tabular}}}}}}    & Linear                         & -& -& -& {params[1][0][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & Polynomial                                               & {params[1][1][1]:.2f}& {params[1][1][2]:.2f}& {params[1][1][3]:.2f}& {params[1][1][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & \\begin{{tabular}}[c]{{@{{}}l@{{}}}}Radial\\\\ basis\\end{{tabular}}  & -& {params[1][2][2]:.2f}& -& {params[1][2][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & Sigmoid                                                  & -& {params[1][3][2]:.2f}& {params[1][3][3]:.2f}& {params[1][3][4]:.2f}\\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Virginica\\\\ vs \\\\ Setosa\\end{{tabular}}}}}}     & Linear                         & -& -& -& {params[2][0][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & Polynomial                                               & {params[2][1][1]:.2f}& {params[2][1][2]:.2f}& {params[2][1][3]:.2f}& {params[2][1][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & \\begin{{tabular}}[c]{{@{{}}l@{{}}}}Radial\\\\ basis\\end{{tabular}}   & -& {params[2][2][2]:.2f}& -& {params[2][2][4]:.2f}\\\\ \\cline{{2-6}} 
                                                                                               & Sigmoid                                                  & -& {params[2][3][2]:.2f}& {params[2][3][3]:.2f}& {params[2][3][4]:.2f}\\\\ \\hline
\\end{{tabular}}
\\caption{{Table showing the parameters with the lowest validation errors}}
\\label{{tbl:PB:LowVErr}}
\\end{{table}}
"""

tbl1=tableFormat.format(**{"params":bVParams2})


with open("Output/ParamsTabel.tex",'w') as fp :
    fp.write(tbl1)
    
    
    
    
    
meanTable="""
\\begin{{table}}[H]
\\centering
\\begin{{tabular}}{{|c|l|l|l|l|l|}}
\\hline
\\multirow{{2}}{{*}}{{\\textbf{{Problem}}}}                                                              & \\multicolumn{{1}}{{c|}}{{\\multirow{{2}}{{*}}{{\\textbf{{$C$}}}}}} & \\multicolumn{{4}}{{c|}}{{\\textbf{{Mean accuracies}}}}    \\\\ \\cline{{3-6}} 
                                                                                               & \\multicolumn{{1}}{{c|}}{{}}                              & Linear & Polynomial & Radial basis & Sigmoid \\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Versicolor\\\\ vs \\\\ Virginica\\end{{tabular}}}}}}   & {ctext1:.2f}&{meanVals[0][0][0]:.2f}&{meanVals[0][1][0]:.2f}&{meanVals[0][2][0]:.2f}&{meanVals[0][3][0]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext2:.2f}&{meanVals[0][0][1]:.2f}&{meanVals[0][1][1]:.2f}&{meanVals[0][2][1]:.2f}&{meanVals[0][3][1]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext3:.2f}&{meanVals[0][0][2]:.2f}&{meanVals[0][1][2]:.2f}&{meanVals[0][2][2]:.2f}&{meanVals[0][3][2]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext4:.2f}&{meanVals[0][0][3]:.2f}&{meanVals[0][1][3]:.2f}&{meanVals[0][2][3]:.2f}&{meanVals[0][3][3]:.2f}\\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Versicolor\\\\ vs \\\\ Setosa\\end{{tabular}}}}}}      & {ctext1:.2f}&{meanVals[1][0][0]:.2f}&{meanVals[1][1][0]:.2f}&{meanVals[1][2][0]:.2f}&{meanVals[1][3][0]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext2:.2f}&{meanVals[1][0][1]:.2f}&{meanVals[1][1][1]:.2f}&{meanVals[1][2][1]:.2f}&{meanVals[1][3][1]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext3:.2f}&{meanVals[1][0][2]:.2f}&{meanVals[1][1][2]:.2f}&{meanVals[1][2][2]:.2f}&{meanVals[1][3][2]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext4:.2f}&{meanVals[1][0][3]:.2f}&{meanVals[1][1][3]:.2f}&{meanVals[1][2][3]:.2f}&{meanVals[1][3][3]:.2f}\\\\ \\hline
\\multirow{{4}}{{*}}{{\\textbf{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Virginica\\\\ vs \\\\ Setosa\\end{{tabular}}}}}}       & {ctext1:.2f}&{meanVals[2][0][0]:.2f}&{meanVals[2][1][0]:.2f}&{meanVals[2][2][0]:.2f}&{meanVals[2][3][0]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext2:.2f}&{meanVals[2][0][1]:.2f}&{meanVals[2][1][1]:.2f}&{meanVals[2][2][1]:.2f}&{meanVals[2][3][1]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext3:.2f}&{meanVals[2][0][2]:.2f}&{meanVals[2][1][2]:.2f}&{meanVals[2][2][2]:.2f}&{meanVals[2][3][2]:.2f}\\\\ \\cline{{2-6}} 
																														   & {ctext4:.2f}&{meanVals[2][0][3]:.2f}&{meanVals[2][1][3]:.2f}&{meanVals[2][2][3]:.2f}&{meanVals[2][3][3]:.2f}\\\\ \\hline
\\end{{tabular}}
\\caption{{Mean accuracies of the various parameters}}
\\label{{tbl:PB:mean}}
\\end{{table}}
"""

Ocvals=CostValues[CValsToShow]
tbl2=meanTable.format(**{"meanVals":mean[:,:,CValsToShow],
                         "ctext1":Ocvals[0],
                         "ctext2":Ocvals[1],
                         "ctext3":Ocvals[2],
                         "ctext4":Ocvals[3]})


with open("Output/MeanTabel.tex",'w') as fp :
    fp.write(tbl2)