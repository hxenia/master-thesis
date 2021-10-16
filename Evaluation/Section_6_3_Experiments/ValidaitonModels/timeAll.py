import os
import subprocess

#import theories
theoryFolder = ''
theoryNames = open(theoryFolder + 'theoryNames', 'r')
names = theoryNames.readline()
theories = names.split(',')

allLemmas = ["executable_oneSignature",
             "executable_twoSignatures", "executable_twoSignatures_nice",
           "aliveness", "aliveness_message", "weak_agreement_falsified",
           "no_ZerosplittingAttack", "no_RogueKeyAttack"]

tamarin = "~/.local/bin/tamarin-prover"

time = "5" #Timeout in seconds

outputTableName = "output/measurements_withTimeout"+time+".csv"
outputTable = open(outputTableName, 'w')
outputTable.write("theory")
for lemma in allLemmas:
    outputTable.write(", " + lemma)
outputTable.write("\n")

#go through the theories
for theory in theories:

    print("\ntheory: " + theory)

    outputTable.write(theory)
    #go through lemmas
    
    for lemma in allLemmas:
        print("\nlemma: "+lemma)

        #evaluate this lemma       
        outputFileName = "output/tamarinOutput_timeout"+time+"/"+theory[:-6]+"_"+lemma
        outputFile = open(outputFileName, 'a')
        outputFile.write(outputFileName + "\n ============================\n \n")
        
        tamarinResult = subprocess.run(["timeout", time+"s", "/usr/bin/time", "-o", outputFileName, "-p", tamarin, "+RTS", "-N4", "-RTS", "--prove="+lemma, "--quit-on-warning", theoryFolder+theory]
                                       , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if (tamarinResult.returncode == 124):
            #timed out
            print("time out")
            outputTable.write(", timed out after " + time + " seconds")
            
            outputFile.write(tamarinResult.stdout.decode("utf-8"))
            outputFile.close
        else:
            print("tamarin done")
            
            outputFile.write(tamarinResult.stdout.decode("utf-8"))
            outputFile.close
            
            resultFile = open(outputFileName, 'r')
            real =  resultFile.readline()
            user =  resultFile.readline()
            sys =  resultFile.readline() 
            if not(real.startswith("real")):
                #error occured
                outputTable.write(",something went wrong: " + real[:-1])
                print("error")
            else:
                #check that verified
                resultLine = resultFile.readline()
                while not (resultLine.startswith("summary of summaries:")):
                    resultLine = resultFile.readline()
                    
                while not (resultLine.startswith('  ' + lemma)) and not(resultLine.startswith("=====")):
                    resultLine = resultFile.readline()

                if resultLine.startswith("===="):
                    #lemma does not exist in theory
                    outputTable.write(", lemma missing")
                    print("lemma missing")
                elif "_falsified" in resultLine and "found trace" in resultLine:
                    #lemma correctly falsified
                    outputTable.write("," + real[:-1] + ' '+ user[:-1]  + ' ' + sys[:-1])
                    print("falsified")
                elif not("_falsified" in resultLine) and "verified" in resultLine:
                    #lemma verified
                    outputTable.write("," + real[:-1] + ' '+ user[:-1]  + ' ' + sys[:-1])
                    print("verified")
                else:
                    #lemma not verified (some thing went wrong)  
                    outputTable.write(",something went wrong: " + resultLine[:-1])
                    print("error")
                    

        
    print("\n"+theory + " done\n=================")   
    outputTable.write("\n")


outputTable.close()

